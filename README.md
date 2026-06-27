# Leads QualiFlow - Complete Service

## 📁 What's Here

| Folder | Contents |
|---|---|
| **Root /** (14 HTML files) | Live website — home, features, pricing, login, Anna, AI Clone |
| **styles.css + app.js** | Styling + full interactivity (voice nav, captions, auth) |
| **sitemap.xml + robots.txt** | SEO optimization |
| **legal/** | 50-state legal docs (privacy, terms, cookies, disclaimers, ADA, PA) |
| **content/** | Chatbot scripts, email sequences, guides, examples |
| **brand/** | Logo, favicon, brand guide |
| **backend/** | Python Flask API + document generator |

## 🚀 Deploy the Static Site (Already Live)

**https://homeenhanced15-beep.github.io/QualiFlow/**

To move it anywhere else — just upload all the HTML/CSS/JS files to any host.

## ⚙️ Deploy the Backend (For Forms + Document Generation)

### Option A: Render (Free — easiest)
1. Go to https://render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repo
4. Set: Root Directory = `backend`, Build Command = `pip install -r requirements.txt`, Start Command = `gunicorn app:app`
5. Deploy

### Option B: PythonAnywhere (Free)
1. Upload `/backend/` folder
2. Open a Bash console: `pip install -r requirements.txt`
3. Set up a web app pointing to `app.py`

### Option C: Any VPS
```bash
cd backend
pip install -r requirements.txt
python app.py
```

## 🔌 API Endpoints

| Endpoint | Method | What it does |
|---|---|---|
| `/api/generate` | POST | Submit questionnaire → get documents |
| `/api/leads` | GET/POST | Manage qualified leads |
| `/download/<id>/<type>` | GET | Download config/scoring/clone docs |
| `/admin` | GET | Admin dashboard |
| `/admin/leads` | GET | All lead records |
| `/admin/clients` | GET | All client records |