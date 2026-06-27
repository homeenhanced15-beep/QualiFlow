#!/usr/bin/env python3
"""Leads QualiFlow - Backend API Server
Deploy to: Render, PythonAnywhere, Railway, Heroku, or any Python host.

Quick deploy:
  pip install -r requirements.txt
  python app.py
"""

import os, json, uuid, tempfile, html
from datetime import datetime
from flask import Flask, request, jsonify, render_template_string, send_file
from flask_cors import CORS
from generator import DocumentGenerator
from storage import LeadStore, ClientStore, SubmissionStore

app = Flask(__name__)
CORS(app)
documents_store = {}

@app.route('/')
def home():
    return jsonify({
        'service': 'Leads QualiFlow API',
        'version': '2.0.0',
        'endpoints': {
            'POST /api/generate': 'Submit questionnaire answers, get documents',
            'POST /api/leads': 'Add a qualified lead to the system',
            'GET /api/leads': 'List all qualified leads',
            'GET /api/doc/<id>': 'View generated documents in browser',
            'GET /download/<id>/<type>': 'Download (chatbot/scoring/clone/all/zip)',
            'GET /admin': 'Admin dashboard summary',
            'GET /admin/leads': 'All lead records',
            'GET /admin/clients': 'All client records',
        }
    })

@app.route('/api/generate', methods=['POST'])
def generate():
    """Receive questionnaire answers and generate documents."""
    try:
        data = request.get_json() or {}
        required = ['business_name', 'industry']
        missing = [f for f in required if not data.get(f)]
        if missing:
            return jsonify({'error': f'Missing: {", ".join(missing)}'}), 400

        gen = DocumentGenerator(data)
        docs = gen.generate_all()
        doc_id = str(uuid.uuid4())[:8]
        documents_store[doc_id] = {
            'docs': docs, 'answers': data,
            'created_at': datetime.now().isoformat()
        }

        try: SubmissionStore.save(data, doc_id)
        except: pass

        return jsonify({
            'success': True, 'doc_id': doc_id,
            'business_name': data.get('business_name'),
            'view_url': f'/api/doc/{doc_id}',
            'download_urls': {
                'chatbot': f'/download/{doc_id}/chatbot',
                'scoring': f'/download/{doc_id}/scoring',
                'clone': f'/download/{doc_id}/clone',
                'all': f'/download/{doc_id}/all',
            }
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/leads', methods=['GET', 'POST'])
def handle_leads():
    if request.method == 'POST':
        try:
            data = request.get_json() or {}
            lead = LeadStore.add_lead(data)
            return jsonify({'success': True, 'lead': lead}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        client_id = request.args.get('client_id')
        status = request.args.get('status')
        leads = LeadStore.get_leads(client_id, status)
        counts = LeadStore.count_by_status(client_id)
        return jsonify({'leads': leads, 'counts': counts})

@app.route('/api/doc/<doc_id>')
def view_doc(doc_id):
    """View generated documents in browser."""
    if doc_id not in documents_store:
        return f"<h1>Document not found</h1><p>ID: {doc_id}</p><a href='/'>Back</a>", 404
    
    entry = documents_store[doc_id]
    docs = entry['docs']
    biz = html.escape(docs['business_name'])
    content = html.escape(docs['chatbot_config'])
    
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Document - {biz}</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:'Courier New',monospace;background:#1a1a2e;color:#e0e0e0;padding:2rem}}
pre{{background:#0d0d1a;padding:2rem;border-radius:8px;white-space:pre-wrap;font-size:14px;line-height:1.6;border:1px solid #333}}
h1{{color:#00a86b;margin-bottom:1rem;font-family:Arial,sans-serif}}
.actions{{margin:2rem 0;display:flex;gap:1rem;flex-wrap:wrap}}
.btn{{padding:0.8rem 1.5rem;border-radius:4px;text-decoration:none;font-weight:bold;display:inline-block}}
.btn-primary{{background:#0057b7;color:white}}
.btn-success{{background:#00a86b;color:white}}
.nav{{margin-bottom:2rem}}
.nav a{{color:#00a86b;text-decoration:none;margin-right:1rem}}
.badge{{background:#00a86b;color:white;padding:0.25rem 0.75rem;border-radius:4px;font-size:0.8rem}}
.meta{{margin-bottom:2rem;color:#888;font-family:Arial,sans-serif}}
</style></head><body>
<div class="nav"><a href="/">&larr; API</a><span class="badge">{biz}</span></div>
<h1>Chatbot Configuration</h1>
<div class="meta">Generated: {html.escape(docs['generated_at'])}</div>
<div class="actions">
<a href="/download/{doc_id}/chatbot" class="btn btn-primary">Download Config</a>
<a href="/download/{doc_id}/scoring" class="btn btn-success">Download Scoring</a>
<a href="/download/{doc_id}/all" class="btn btn-primary">Download All</a>
</div>
<pre>{content}</pre></body></html>"""

@app.route('/download/<doc_id>/<doc_type>')
def download(doc_id, doc_type):
    if doc_id not in documents_store:
        return jsonify({'error': 'Not found'}), 404
    
    entry = documents_store[doc_id]
    docs = entry['docs']
    business = docs['business_name'].replace(' ', '_')
    
    doc_map = {
        'chatbot': 'chatbot_config',
        'scoring': 'scoring_criteria',
        'clone': 'ai_clone_brief',
    }
    
    if doc_type == 'all':
        content = f"""Leads QualiFlow - Generated Documents
Business: {docs['business_name']}
Generated: {docs['generated_at']}
{'='*60}\n\n{docs['chatbot_config']}\n\n{docs['scoring_criteria']}\n\n{docs['ai_clone_brief']}"""
        filename = f'{business}_Complete_Docs.txt'
    elif doc_type in doc_map:
        content = docs[doc_map[doc_type]]
        filename = f'{business}_{doc_type.capitalize()}.txt'
    else:
        return jsonify({'error': 'Invalid type'}), 400
    
    f = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt', encoding='utf-8')
    f.write(content)
    f.close()
    
    return send_file(f.name, as_attachment=True, download_name=filename, mimetype='text/plain')

@app.route('/admin')
def admin():
    counts = {}
    try: 
        leads = LeadStore.get_leads()
        counts = LeadStore.count_by_status()
        sub_count = len(SubmissionStore.get_all())
    except: 
        leads = []
        sub_count = 0
    
    client_count = 0
    try: client_count = len(ClientStore.get_clients())
    except: pass
    
    return f"""<!DOCTYPE html><html lang="en"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>Admin - Leads QualiFlow</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0}}
body{{font-family:Arial,sans-serif;background:#f7f9fc;color:#1a1a2e;padding:2rem}}
h1{{color:#0057b7}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:1.5rem;margin:2rem 0}}
.card{{background:white;padding:1.5rem;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.1)}}
.card h3{{color:#0057b7;margin-bottom:0.5rem}}
.card .number{{font-size:2rem;font-weight:bold;color:#00a86b}}
table{{width:100%;border-collapse:collapse;margin-top:1rem}}
th,td{{text-align:left;padding:0.75rem;border-bottom:1px solid #ddd}}
th{{background:#0057b7;color:white}}
.nav a{{color:#0057b7;text-decoration:none;margin-right:1rem}}
</style></head><body>
<h1>Leads QualiFlow Admin</h1>
<div class="nav"><a href="/">API Home</a><a href="/admin/leads">All Leads</a><a href="/admin/clients">All Clients</a></div>
<div class="cards">
<div class="card"><h3>Total Leads</h3><div class="number">{len(leads)}</div></div>
<div class="card"><h3>New</h3><div class="number">{counts.get('new',0)}</div></div>
<div class="card"><h3>Closed</h3><div class="number">{counts.get('closed',0)}</div></div>
<div class="card"><h3>Submissions</h3><div class="number">{sub_count}</div></div>
<div class="card"><h3>Clients</h3><div class="number">{client_count}</div></div>
</div>
<table><thead><tr><th>Business</th><th>Lead Score</th><th>Tier</th><th>Status</th><th>Date</th></tr></thead>
<tbody>{"".join(f'<tr><td>{l.get("company","N/A")}</td><td>{l.get("score",0)}</td><td>{l.get("tier","N/A")}</td><td>{l.get("status","new")}</td><td>{l.get("created_at","N/A")[:10]}</td></tr>' for l in leads[:20])}</tbody></table>
</body></html>"""

@app.route('/admin/leads')
def admin_leads():
    try: leads = LeadStore.get_leads()
    except: leads = []
    rows = "".join(f'<tr><td>{l.get("name","")}</td><td>{l.get("company","")}</td><td>{l.get("email","")}</td><td>{l.get("score",0)}</td><td>{l.get("tier","")}</td><td>{l.get("status","")}</td><td>{l.get("created_at","")[:10]}</td></tr>' for l in leads)
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>All Leads</title>
<style>body{{font-family:Arial,sans-serif;padding:2rem}}table{{width:100%;border-collapse:collapse}}th,td{{padding:0.5rem;text-align:left;border-bottom:1px solid #ddd}}th{{background:#0057b7;color:white}}</style></head><body>
<h1>All Leads ({len(leads)})</h1><a href="/admin">&larr; Back</a>
<table><thead><tr><th>Name</th><th>Company</th><th>Email</th><th>Score</th><th>Tier</th><th>Status</th><th>Date</th></tr></thead><tbody>{rows}</tbody></table></body></html>"""

@app.route('/admin/clients')
def admin_clients():
    try: clients = ClientStore.get_clients()
    except: clients = []
    rows = "".join(f'<tr><td>{c.get("name","")}</td><td>{c.get("company","")}</td><td>{c.get("email","")}</td><td>{c.get("package","")}</td><td>{c.get("created_at","")[:10]}</td></tr>' for c in clients)
    return f"""<!DOCTYPE html><html><head><meta charset="UTF-8"><title>All Clients</title>
<style>body{{font-family:Arial,sans-serif;padding:2rem}}table{{width:100%;border-collapse:collapse}}th,td{{padding:0.5rem;text-align:left;border-bottom:1px solid #ddd}}th{{background:#0057b7;color:white}}</style></head><body>
<h1>All Clients ({len(clients)})</h1><a href="/admin">&larr; Back</a>
<table><thead><tr><th>Name</th><th>Company</th><th>Email</th><th>Package</th><th>Date</th></tr></thead><tbody>{rows}</tbody></table></body></html>"""

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'false').lower() == 'true'
    app.run(host='0.0.0.0', port=port, debug=debug)