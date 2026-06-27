import os, re

os.chdir('/home/team/shared/leads_qualiflow')

BASE = 'https://homeenhanced15-beep.github.io/QualiFlow'

page_meta = {
    'index.html': {
        'title': 'Leads QualiFlow | Pre-Qualified Leads Delivered Monthly',
        'desc': 'Buy ready-to-buy qualified leads in fixed-price packages. Our AI chatbots capture, score & deliver high-intent prospects. ADA accessible, 50-state compliant.',
        'img': 'og-image.png'
    },
    'features.html': {
        'title': 'Features | Leads QualiFlow — AI Lead Qualification',
        'desc': 'Multi-language chatbots, BANT scoring, automated email follow-ups, AI Clone, and 28 add-on services. Fully ADA accessible lead generation platform.',
        'img': 'og-image.png'
    },
    'pricing.html': {
        'title': 'Pricing & Packages | Leads QualiFlow',
        'desc': 'Lead packages from $397/mo (25 leads) to $3,997/mo (500+ leads). 28 add-on services starting at $47/mo. Pre-qualified leads delivered monthly.',
        'img': 'og-image.png'
    },
    'how-it-works.html': {
        'title': 'How It Works | Leads QualiFlow — Lead Qualification Process',
        'desc': 'See how a lead goes from chatbot interaction to qualified buyer in 4 steps. Our AI scores leads by budget, authority, need & timeline.',
        'img': 'og-image.png'
    },
    'anna.html': {
        'title': 'Meet Anna AI Expert | Leads QualiFlow',
        'desc': 'Meet Anna, your AI onboarding expert. Answer a 6-step questionnaire and Anna configures your custom lead qualification chatbot automatically.',
        'img': 'og-image.png'
    },
    'ai-clone.html': {
        'title': 'AI Clone Chat | Leads QualiFlow — Talk to Our AI',
        'desc': 'Interact with an AI business representative clone trained on your company knowledge. Get qualified instantly through intelligent conversation.',
        'img': 'og-image.png'
    },
    'questionnaire.html': {
        'title': 'AI Assessment | Leads QualiFlow — Build Your Chatbot',
        'desc': 'Complete Anna\'s 6-step assessment to build your customized lead qualification chatbot with AI Clone support.',
        'img': 'og-image.png'
    },
    'guides.html': {
        'title': 'Guides & Documentation | Leads QualiFlow',
        'desc': 'Learn how to use the Leads QualiFlow client dashboard, manage leads, integrate with CRM, and understand lead score tiers.',
        'img': 'og-image.png'
    },
    'login.html': {
        'title': 'Client Login | Leads QualiFlow',
        'desc': 'Secure client login with password, Google sign-in, biometrics, or Anna verification. Access your lead dashboard.',
        'img': 'og-image.png'
    },
    'privacy.html': {
        'title': 'Privacy Policy | Leads QualiFlow — 50-State Compliant',
        'desc': 'Leads QualiFlow privacy policy — CCPA, VCDPA, CPA, CTDPA, and Pennsylvania compliant. How we collect, use, and protect your data.',
        'img': 'og-image.png'
    },
    'terms.html': {
        'title': 'Terms of Service | Leads QualiFlow',
        'desc': 'Terms of service for Leads QualiFlow lead purchase packages, add-on services, and account management.',
        'img': 'og-image.png'
    },
    'cookies.html': {
        'title': 'Cookie Policy | Leads QualiFlow',
        'desc': 'Cookie policy for Leads QualiFlow. Learn about essential, functional, and advertising cookies used on our platform.',
        'img': 'og-image.png'
    },
    'disclaimers.html': {
        'title': 'Disclaimers | Leads QualiFlow',
        'desc': 'Legal disclaimers for lead quality, scoring methodology, and service limitations for Leads QualiFlow lead generation platform.',
        'img': 'og-image.png'
    },
    'accessibility.html': {
        'title': 'Accessibility Statement | Leads QualiFlow — WCAG 2.1 AA',
        'desc': 'Leads QualiFlow is committed to WCAG 2.1 AA compliance. Voice navigation, captions, screen reader support, and keyboard accessibility.',
        'img': 'og-image.png'
    }
}

for fname, meta in page_meta.items():
    if not os.path.exists(fname):
        print(f"SKIP {fname}")
        continue
    
    with open(fname, 'r') as f:
        html = f.read()
    
    title = meta['title']
    desc = meta['desc']
    img = f"{BASE}/{meta['img']}"
    url = f"{BASE}/{fname}" if fname != 'index.html' else f"{BASE}/"
    
    seo_block = f'''
    <!-- SEO Meta Tags -->
    <meta name="description" content="{desc}">
    <meta name="robots" content="index, follow">
    <link rel="canonical" href="{url}">
    
    <!-- Open Graph Tags -->
    <meta property="og:type" content="website">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{desc}">
    <meta property="og:url" content="{url}">
    <meta property="og:image" content="{img}">
    <meta property="og:site_name" content="Leads QualiFlow">
    <meta property="og:locale" content="en_US">
    
    <!-- Twitter Card Tags -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="{title}">
    <meta name="twitter:description" content="{desc}">
    <meta name="twitter:image" content="{img}">
    
    <!-- Breadcrumb Structured Data -->
    <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [{{
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "{BASE}/"
      }}, {{
        "@type": "ListItem",
        "position": 2,
        "name": "{title.split('|')[0].strip()}",
        "item": "{url}"
      }}]
    }}
    </script>'''
    
    # Replace existing meta description if present
    if 'name="description"' in html:
        html = re.sub(r'<meta name="description" content="[^"]*">', '', html)
    
    # Check if SEO block already exists
    if 'og:title' in html:
        print(f"SKIP (already SEO'd): {fname}")
        continue
    
    # Inject before </head>
    html = html.replace('</head>', f'{seo_block}\n</head>')
    
    with open(fname, 'w') as f:
        f.write(html)
    
    print(f"✅ SEO: {fname}")

print("\n=== DONE ===")