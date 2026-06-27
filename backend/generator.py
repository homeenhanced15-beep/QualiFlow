"""Leads QualiFlow - Document Generation Engine
Takes questionnaire responses and generates customized legal documents, 
chatbot configuration specs, and qualification criteria sheets."""

import os
import json
from datetime import datetime

class DocumentGenerator:
    """Core engine that transforms questionnaire answers into documents."""
    
    def __init__(self, answers: dict):
        self.answers = answers
        self.business_name = answers.get('business_name', 'Your Business')
        self.industry = answers.get('industry', 'General')
        self.company_size = answers.get('company_size', '1-10')
        self.website = answers.get('website_url', '')
        
    # ──────────────────────────────────────────────
    #  1. CHATBOT CONFIGURATION SPEC
    # ──────────────────────────────────────────────
    def generate_chatbot_config(self) -> str:
        """Generate a chatbot configuration document based on questionnaire answers."""
        a = self.answers
        config = f"""
╔══════════════════════════════════════════════════════════════╗
║            LEADS QUALIFLOW - CHATBOT CONFIGURATION          ║
╠══════════════════════════════════════════════════════════════╣
║  Generated:     {datetime.now().strftime('%Y-%m-%d %H:%M')}                   
║  Business:      {a.get('business_name', 'N/A')}                             
║  Industry:      {a.get('industry', 'N/A')}                                  
║  Website:       {a.get('website_url', 'N/A')}                              
╚══════════════════════════════════════════════════════════════╝

┌────────────────────────────────────────────────────────────┐
│ 1. BUSINESS PROFILE                                         │
└────────────────────────────────────────────────────────────┘
  Company Name:    {a.get('business_name', 'N/A')}
  Industry:        {a.get('industry', 'N/A')}
  Company Size:    {a.get('company_size', 'N/A')}
  Website:         {a.get('website_url', 'N/A')}

┌────────────────────────────────────────────────────────────┐
│ 2. IDEAL CUSTOMER PROFILE (ICP)                             │
└────────────────────────────────────────────────────────────┘
  Target Industries: {', '.join(a.get('target_industries', ['All'])) if isinstance(a.get('target_industries'), list) else a.get('target_industries', 'All')}
  Target Size:       {a.get('target_size', 'Any')}
  Decision Maker:    {a.get('decision_maker', 'N/A')}
  Pain Points:       {a.get('pain_points', 'N/A')}

┌────────────────────────────────────────────────────────────┐
│ 3. QUALIFICATION CRITERIA                                   │
└────────────────────────────────────────────────────────────┘
  Min Budget:        {a.get('min_budget', 'Not specified')}
  Timeline:          {a.get('timeline', 'Not specified')}
  Authority Needed:  {a.get('authority', 'Not specified')}
  
  Custom Questions:
    Q1: {a.get('custom_q1', 'N/A')}
    Q2: {a.get('custom_q2', 'N/A')}
    Q3: {a.get('custom_q3', 'N/A')}

┌────────────────────────────────────────────────────────────┐
│ 4. PREFERENCES                                              │
└────────────────────────────────────────────────────────────┘
  Languages:         {', '.join(a.get('languages', ['English'])) if isinstance(a.get('languages'), list) else 'English'}
  Delivery Method:   {a.get('delivery_method', 'Email')}
  Follow-up Cadence: {a.get('follow_up', 'Not specified')}
  Territory:         {a.get('territory', 'Nationwide')}

┌────────────────────────────────────────────────────────────┐
│ 5. AI CLONE CONFIGURATION                                   │
└────────────────────────────────────────────────────────────┘
  AI Clone Enabled:  {'YES' if a.get('ai_clone') == 'yes' else 'NO'}
  Communication Style: {a.get('comm_style', 'Professional')}
  Sales Philosophy:    {a.get('sales_philosophy', 'N/A')}
  Key Talking Points:  {a.get('key_points', 'N/A')}
  Common Objection:    {a.get('objection', 'N/A')}
  Closing Line:        {a.get('closing_line', 'N/A')}
"""
        return config

    # ──────────────────────────────────────────────
    #  2. LEAD SCORING CRITERIA SHEET
    # ──────────────────────────────────────────────
    def generate_scoring_criteria(self) -> str:
        """Generate a lead scoring matrix tailored to the business."""
        industry_weights = {
            'SaaS': {'intent': 20, 'budget': 30, 'timeline': 25, 'authority': 20, 'size': 15},
            'Real Estate': {'intent': 25, 'budget': 20, 'timeline': 30, 'authority': 15, 'size': 10},
            'Financial Services': {'intent': 20, 'budget': 30, 'timeline': 20, 'authority': 25, 'size': 15},
            'Legal': {'intent': 20, 'budget': 25, 'timeline': 20, 'authority': 25, 'size': 10},
            'Medical': {'intent': 25, 'budget': 20, 'timeline': 25, 'authority': 20, 'size': 10},
            'Home Services': {'intent': 30, 'budget': 15, 'timeline': 30, 'authority': 15, 'size': 10},
        }
        weights = industry_weights.get(self.industry, industry_weights['SaaS'])
        
        total = sum(weights.values())
        
        return f"""
╔══════════════════════════════════════════════════════════════╗
║         LEAD SCORING MATRIX - {self.business_name.upper():>30}  ║
╠══════════════════════════════════════════════════════════════╣
║  Industry: {self.industry:<55}║
║  Max Score: {total}/100                                         ║
║  Qualified Threshold: 60/100                                   ║
╚══════════════════════════════════════════════════════════════╝

SCORING CATEGORIES:
┌─────────────────────────┬──────────┬────────────────────────┐
│ Category                │ Weight   │ Scoring Logic          │
├─────────────────────────┼──────────┼────────────────────────┤
│ Intent / Need           │    {weights['intent']:>2} pts │ Product/Service match     │
│ Budget                  │    {weights['budget']:>2} pts │ Within target range       │
│ Timeline / Urgency      │    {weights['timeline']:>2} pts │ < 30 days = max points    │
│ Decision Authority      │    {weights['authority']:>2} pts │ Decision-maker = max      │
│ Company Size / Fit      │    {weights['size']:>2} pts │ ICP match                 │
├─────────────────────────┼──────────┼────────────────────────┤
│ TOTAL POSSIBLE          │    {total:>2} pts │                           │
└─────────────────────────┴──────────┴────────────────────────┘

LEAD TIERS:
  🔥 Elite (80-{total}):    Immediate senior rep contact < 1 hour
  🟧 Hot (60-79):         Sales rep follow-up within 4 hours
  🟩 Warm (40-59):        SDR follow-up within 24 hours
  🟦 Cold (0-39):         Automated nurture sequence

CUSTOM QUALIFICATION QUESTIONS:
  1. {self.answers.get('custom_q1', 'What is your primary need?')}
  2. {self.answers.get('custom_q2', 'What is your timeline?')}
  3. {self.answers.get('custom_q3', 'What is your budget range?')}
"""

    # ──────────────────────────────────────────────
    #  3. AI CLONE BRIEF
    # ──────────────────────────────────────────────
    def generate_ai_clone_brief(self) -> str:
        """Generate an AI clone personality brief for training."""
        a = self.answers
        if a.get('ai_clone') != 'yes':
            return "\n[AI Clone not enabled - skipping brief]\n"
            
        return f"""
╔══════════════════════════════════════════════════════════════╗
║              AI CLONE PERSONALITY BRIEF                      ║
║              {self.business_name.upper():>35}               ║
╠══════════════════════════════════════════════════════════════╣
║  Created: {datetime.now().strftime('%Y-%m-%d')}                                  ║
╚══════════════════════════════════════════════════════════════╝

COMMUNICATION STYLE: {a.get('comm_style', 'Professional')}

SALES PHILOSOPHY:
{a.get('sales_philosophy', 'Not specified')}

KEY TALKING POINTS:
{a.get('key_points', 'Not specified')}

COMMON OBJECTION HANDLING:
{a.get('objection', 'Not specified')}

CLOSING LINE:
{a.get('closing_line', 'Not specified')}

TRAINING DATA:
- Industry: {self.industry}
- Target Customers: {a.get('target_industries', 'All industries')}
- Pain Points Solved: {a.get('pain_points', 'N/A')}
- Territory: {a.get('territory', 'Nationwide')}
- Languages: {', '.join(a.get('languages', ['English'])) if isinstance(a.get('languages'), list) else 'English'}
"""

    # ──────────────────────────────────────────────
    #  4. FULL SUMMARY (all docs combined)
    # ──────────────────────────────────────────────
    def generate_all(self) -> dict:
        """Generate all documents and return as a dictionary."""
        return {
            'chatbot_config': self.generate_chatbot_config(),
            'scoring_criteria': self.generate_scoring_criteria(),
            'ai_clone_brief': self.generate_ai_clone_brief(),
            'generated_at': datetime.now().isoformat(),
            'business_name': self.business_name
        }


if __name__ == '__main__':
    # Test with sample data
    sample = {
        'business_name': 'Acme Software',
        'industry': 'SaaS',
        'company_size': '51-200',
        'website_url': 'https://acme.com',
        'target_industries': ['SaaS', 'Technology'],
        'target_size': '51-200',
        'decision_maker': 'VP of Engineering',
        'pain_points': 'Manual lead qualification takes too long',
        'min_budget': '$25,000 - $100,000',
        'timeline': 'Within 30 days',
        'authority': 'Part of a decision team',
        'custom_q1': 'What project management software do you currently use?',
        'custom_q2': 'How many users would need access?',
        'custom_q3': 'What is driving this purchase now?',
        'languages': ['English', 'Spanish'],
        'delivery_method': 'CRM',
        'follow_up': 'Immediate',
        'territory': 'North America',
        'ai_clone': 'yes',
        'comm_style': 'Consultative',
        'sales_philosophy': 'Focus on ROI and outcomes',
        'key_points': '10x faster qualification, 34% higher close rates',
        'objection': 'Budget concerns - show ROI calculator',
        'closing_line': 'Ready to see the difference?'
    }
    
    gen = DocumentGenerator(sample)
    docs = gen.generate_all()
    print(docs['chatbot_config'])
