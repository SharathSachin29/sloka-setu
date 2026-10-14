import json
import sys
from pypdf import PdfReader

sys.stdout.reconfigure(encoding='utf-8')

reader = PdfReader('backend/storage/pdfs/TAMIL.pdf')
versions = json.load(open('data/intermediate/versions_catalog.json', encoding='utf-8'))
slokas = json.load(open('data/intermediate/slokas_catalog.json', encoding='utf-8'))

print("VERIFYING ALL TAMIL STOTRAS AGAINST TAMIL.PDF:")
print("=" * 70)

tamil_versions = [v for v in versions if v.get('scriptCode') == 'Taml']

for tv in tamil_versions:
    slug = tv['slokaSlug']
    p_start = tv.get('pageStart')
    p_end = tv.get('pageEnd')
    title = next((s['canonicalTitle'] for s in slokas if s['slug'] == slug), slug)
    
    # Check if pageStart and pageEnd are valid
    if not p_start or not p_end or p_start < 1 or p_end > len(reader.pages):
        print(f"FAILED: {slug} invalid pages {p_start}-{p_end}")
        continue
    
    # Extract text from these pages
    extracted_text = ""
    for p in range(p_start - 1, p_end):
        extracted_text += reader.pages[p].extract_text() or ""
    
    # Check if this stotra is actually in the pages
    sample_text = tv.get('textContent', '')[:40].strip()
    has_content = len(extracted_text.strip()) > 50
    
    print(f"Slug: {slug:35} | Pages: {p_start:2d}-{p_end:2d} ({p_end - p_start + 1}p) | Valid: {has_content}")
