import json
import sys
from pypdf import PdfReader

sys.stdout.reconfigure(encoding='utf-8')
versions = json.load(open('data/intermediate/versions_catalog.json', encoding='utf-8'))

for sc, fname in [('Latn', 'ENGLISH.pdf'), ('Telu', 'TELUGU.pdf'), ('Taml', 'TAMIL.pdf')]:
    print(f"\n=================== {fname} ({sc}) ===================")
    r = PdfReader(f'backend/storage/pdfs/{fname}')
    total = len(r.pages)
    print(f"Total pages: {total}")
    sv = [v for v in versions if v.get('scriptCode') == sc]
    for v in sv:
        ps = v.get('pageStart')
        pe = v.get('pageEnd')
        slug = v['slokaSlug']
        print(f"{slug:35} | {ps:2d}-{pe:2d}")
