#!/usr/bin/env python3
"""Leads QualiFlow - Complete Backend API + Admin Dashboard"""
import os, json, uuid, tempfile, html
from datetime import datetime
from flask import Flask, request, jsonify, render_template_string, send_file
from flask_cors import CORS
from generator import DocumentGenerator
from storage import LeadStore, ClientStore, SubmissionStore
from pdf_export import generate_chatbot_config_pdf

app = Flask(__name__)
CORS(app)

# In-memory doc store
documents_store = {}

@app.route('/')
def home():
    return jsonify({
        'service': 'Leads QualiFlow API',
        'version': '2.0.0',
        'endpoints': {
            'POST /api/generate': 'Submit questionnaire -> get docs',
            'POST /api/leads': 'Add a qualified lead',
            'GET /api/leads': 'List leads',
            'POST /api/questionnaire': 'Form submit from questionnaire.html',
            'GET /api/doc/<id>': 'View generated documents',
            'GET /download/<id>/<type>': 'Download (chatbot/scoring/clone/all/pdf)',
            'GET /admin': 'Admin dashboard',
            'GET /admin/leads': 'All leads',
            'GET /admin/clients': 'All clients',
        }
    })

@app.route('/api/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json() or {}
        required = ['business_name', 'industry']
        missing = [f for f in required if not data.get(f)]
        if missing:
            return jsonify({'error': f'Missing: {", ".join(missing)}'}), 400

        gen = DocumentGenerator(data)
        docs = gen.generate_all()
        doc_id = str(uuid.uuid4())[:8]
        documents_store[doc_id] = {'docs': docs, 'answers': data, 'created_at': datetime.now().isoformat()}

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
                'pdf': f'/download/{doc_id}/pdf'
            }
        }), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
