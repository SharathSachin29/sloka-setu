import sys
from pypdf import PdfReader

sys.stdout.reconfigure(encoding='utf-8')
reader = PdfReader('backend/storage/pdfs/TAMIL.pdf')

for page_idx, page in enumerate(reader.pages):
    text = page.extract_text() or ''
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    header_sample = lines[:4] if lines else []
    footer_sample = lines[-2:] if lines else []
    print(f"--- PAGE {page_idx + 1} ---")
    print("TOP:", " | ".join(header_sample))
    print("BOTTOM:", " | ".join(footer_sample))
    print()
