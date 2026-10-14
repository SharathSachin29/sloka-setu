import json
import sys
from pypdf import PdfReader

sys.stdout.reconfigure(encoding='utf-8')

slokas = json.load(open('data/intermediate/slokas_catalog.json', encoding='utf-8'))
versions = json.load(open('data/intermediate/versions_catalog.json', encoding='utf-8'))
reader = PdfReader('backend/storage/pdfs/TAMIL.pdf')
total_pages = len(reader.pages)
print(f"Total pages in TAMIL.pdf: {total_pages}\n")

for s in slokas:
    slug = s['slug']
    v_taml = [v for v in versions if v['slokaSlug'] == slug and v.get('scriptCode') == 'Taml']
    if v_taml:
        vt = v_taml[0]
        p_start = vt.get('pageStart')
        p_end = vt.get('pageEnd')
        print(f"{slug:35} | Pages: {p_start} to {p_end} | {s['canonicalTitle']}")
    else:
        print(f"{slug:35} | NO TAMIL VERSION")
