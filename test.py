from fpdf import FPDF
from bidi.algorithm import get_display
from arabic_reshaper import reshape

class PDF(FPDF):
    def header(self):
        self.set_font('DejaVu', 'B', 12)
        self.cell(0, 10, 'Arabic Text Example', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('DejaVu', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_body(self, body):
        self.set_font('DejaVu', '', 12)
        reshaped_text = reshape(body)
        bidi_text = get_display(reshaped_text)
        self.multi_cell(0, 10, bidi_text)
        self.ln()

def text_to_pdf(text, pdf_file, font_path):
    pdf = PDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_font('DejaVu', '', font_path, uni=True)
    pdf.add_font('DejaVu', 'B', font_path.replace(".ttf", "-Bold.ttf"), uni=True)  # Add bold font variant
    pdf.add_font('DejaVu', 'I', font_path.replace(".ttf", "-Italic.ttf"), uni=True)  # Add italic font variant
    
    pdf.chapter_body(text)
    
    pdf.output(pdf_file)

# Example Arabic text
text = "هذا نص باللغة العربية. يمكن استخدام هذه المكتبة لدعم النص العربي."

# Path where you want to save the PDF
pdf_file = 'text_with_arabic.pdf'

# Path to the TTF font file
font_path = 'path/to/DejaVuSans.ttf'

text_to_pdf(text, pdf_file, font_path)

