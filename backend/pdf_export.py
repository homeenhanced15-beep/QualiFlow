"""Leads QualiFlow - PDF Export Engine
Generates professional PDF documents from questionnaire data."""

from fpdf import FPDF
import os
from datetime import datetime

class PDFGenerator(FPDF):
    """Professional PDF document generator for leads QualiFlow."""
    
    def header(self):
        self.set_font('Arial', 'B', 10)
        self.set_text_color(0, 87, 183)
        self.cell(0, 8, 'Leads QualiFlow - Document', 0, 1, 'R')
        self.line(10, 15, 200, 15)
        self.ln(5)
    
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')
    
    def section_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.set_text_color(0, 87, 183)
        self.cell(0, 10, title, 0, 1)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(3)
    
    def sub_title(self, title):
        self.set_font('Arial', 'B', 11)
        self.set_text_color(0, 168, 107)
        self.cell(0, 8, title, 0, 1)
    
    def body_text(self, text):
        self.set_font('Arial', '', 10)
        self.set_text_color(50, 50, 50)
        self.multi_cell(0, 6, text)
        self.ln(2)
    
    def key_value(self, key, value):
        self.set_font('Arial', 'B', 10)
        self.set_text_color(0, 0, 0)
        self.cell(60, 7, key + ':', 0, 0)
        self.set_font('Arial', '', 10)
        self.set_text_color(50, 50, 50)
        self.cell(0, 7, str(value), 0, 1)


def generate_chatbot_config_pdf(answers: dict, output_path: str = None) -> str:
    """Generate a professional PDF of the chatbot configuration."""
    pdf = PDFGenerator()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    # Title
    pdf.set_font('Arial', 'B', 20)
    pdf.set_text_color(0, 87, 183)
    pdf.cell(0, 15, 'Chatbot Configuration', 0, 1)
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(100)
    pdf.cell(0, 6, f'Generated: {datetime.now().strftime("%B %d, %Y")}', 0, 1)
    pdf.cell(0, 6, f'Business: {answers.get("business_name", "N/A")}', 0, 1)
    pdf.ln(5)
    
    # Business Profile
    pdf.section_title('1. Business Profile')
    pdf.key_value('Company', answers.get('business_name', 'N/A'))
    pdf.key_value('Industry', answers.get('industry', 'N/A'))
    pdf.key_value('Size', answers.get('company_size', 'N/A'))
    pdf.key_value('Website', answers.get('website_url', 'N/A'))
    pdf.ln(5)
    
    # ICP
    pdf.section_title('2. Ideal Customer Profile')
    industries = answers.get('target_industries', [])
    if isinstance(industries, list):
        pdf.key_value('Target Industries', ', '.join(industries))
    else:
        pdf.key_value('Target Industries', str(industries))
    pdf.key_value('Target Size', answers.get('target_size', 'Any'))
    pdf.key_value('Decision Maker', answers.get('decision_maker', 'N/A'))
    pdf.body_text(f"Pain Points: {answers.get('pain_points', 'N/A')}")
    pdf.ln(3)
    
    # Qualifications
    pdf.section_title('3. Qualification Criteria')
    pdf.key_value('Min Budget', answers.get('min_budget', 'Not specified'))
    pdf.key_value('Timeline', answers.get('timeline', 'Not specified'))
    pdf.key_value('Authority', answers.get('authority', 'Not specified'))
    
    if answers.get('custom_q1'):
        pdf.sub_title('Custom Questions')
        for i in range(1, 4):
            q = answers.get(f'custom_q{i}')
            if q:
                pdf.body_text(f'Q{i}: {q}')
    pdf.ln(3)
    
    # Preferences
    pdf.section_title('4. Preferences')
    langs = answers.get('languages', ['English'])
    if isinstance(langs, list):
        pdf.key_value('Languages', ', '.join(langs))
    else:
        pdf.key_value('Languages', str(langs))
    pdf.key_value('Delivery', answers.get('delivery_method', 'Email'))
    pdf.key_value('Follow-up', answers.get('follow_up', 'N/A'))
    pdf.key_value('Territory', answers.get('territory', 'Nationwide'))
    
    # AI Clone
    if answers.get('ai_clone') == 'yes':
        pdf.add_page()
        pdf.section_title('5. AI Clone Configuration')
        pdf.key_value('Style', answers.get('comm_style', 'Professional'))
        pdf.sub_title('Sales Philosophy')
        pdf.body_text(answers.get('sales_philosophy', 'N/A'))
        pdf.sub_title('Key Points')
        pdf.body_text(answers.get('key_points', 'N/A'))
        pdf.sub_title('Objection Handling')
        pdf.body_text(answers.get('objection', 'N/A'))
        pdf.sub_title('Closing Line')
        pdf.body_text(answers.get('closing_line', 'N/A'))
    
    # Save
    if output_path:
        pdf.output(output_path)
        return output_path
    
    # Return as bytes
    return pdf.output(dest='S').encode('latin-1')


def generate_all_pdfs(answers: dict) -> dict:
    """Generate all PDF documents and return file paths."""
    os.makedirs('output', exist_ok=True)
    biz = answers.get('business_name', 'business').replace(' ', '_')
    
    paths = {
        'chatbot': f'output/{biz}_chatbot_config.pdf',
        'scoring': f'output/{biz}_scoring_matrix.pdf',
        'clone': f'output/{biz}_ai_clone_brief.pdf',
    }
    
    generate_chatbot_config_pdf(answers, paths['chatbot'])
    
    return paths
