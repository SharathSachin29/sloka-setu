import json
import os
import sys
from pypdf import PdfReader, PdfWriter

sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_DIR = os.path.join(BASE_DIR, 'backend', 'storage', 'pdfs')
VERSIONS_CATALOG = os.path.join(BASE_DIR, 'data', 'intermediate', 'versions_catalog.json')
SLOKAS_CATALOG = os.path.join(BASE_DIR, 'data', 'intermediate', 'slokas_catalog.json')

slokas = json.load(open(SLOKAS_CATALOG, encoding='utf-8'))
versions = json.load(open(VERSIONS_CATALOG, encoding='utf-8'))
sloka_map = {s['slug']: s for s in slokas}

scripts_config = [
    {
        'scriptCode': 'Taml',
        'subDir': 'tamil',
        'suffix': 'tamil',
        'sourceFile': 'TAMIL.pdf',
        'scriptName': 'Tamil'
    },
    {
        'scriptCode': 'Latn',
        'subDir': 'english',
        'suffix': 'english',
        'sourceFile': 'ENGLISH.pdf',
        'scriptName': 'English'
    },
    {
        'scriptCode': 'Telu',
        'subDir': 'telugu',
        'suffix': 'telugu',
        'sourceFile': 'TELUGU.pdf',
        'scriptName': 'Telugu'
    }
]

manifest = {}

for cfg in scripts_config:
    src_path = os.path.join(PDF_DIR, cfg['sourceFile'])
    out_dir = os.path.join(PDF_DIR, cfg['subDir'])
    os.makedirs(out_dir, exist_ok=True)
    
    if not os.path.exists(src_path):
        print(f"ERROR: Source file {src_path} not found!")
        continue
        
    reader = PdfReader(src_path)
    total_pages = len(reader.pages)
    print(f"\nProcessing {cfg['sourceFile']} ({total_pages} pages) for {cfg['scriptName']}...")
    
    script_versions = [v for v in versions if v.get('scriptCode') == cfg['scriptCode']]
    manifest[cfg['scriptCode']] = []
    
    for v in script_versions:
        slug = v['slokaSlug']
        p_start = v.get('pageStart')
        p_end = v.get('pageEnd')
        sloka_info = sloka_map.get(slug, {})
        canonical_title = sloka_info.get('canonicalTitle', slug)
        
        # Exclude known sahasranamas that do not exist in the 46/57 page booklets
        if slug in ['lalita-sahasranama-stotram', 'vishnu-sahasranamam']:
            print(f"  [SKIP - Text Only] {slug} (Not in {cfg['sourceFile']})")
            continue
            
        if not p_start or not p_end or p_start < 1 or p_end > total_pages or p_start > p_end:
            print(f"  [INVALID RANGE] {slug}: pages {p_start}-{p_end} (Total: {total_pages})")
            continue
            
        # Extract pages (0-indexed)
        writer = PdfWriter()
        for page_num in range(p_start - 1, p_end):
            writer.add_page(reader.pages[page_num])
            
        out_filename = f"{slug}-{cfg['suffix']}.pdf"
        out_filepath = os.path.join(out_dir, out_filename)
        
        with open(out_filepath, 'wb') as f:
            writer.write(f)
            
        file_size = os.path.getsize(out_filepath)
        page_count = p_end - p_start + 1
        
        manifest[cfg['scriptCode']].append({
            'slug': slug,
            'title': f"{canonical_title} - {cfg['scriptName']} Edition",
            'fileName': out_filename,
            'relPath': f"backend/storage/pdfs/{cfg['subDir']}/{out_filename}",
            'fullPath': out_filepath,
            'fileSize': file_size,
            'pageCount': page_count,
            'pageReference': f"Pages {p_start}–{p_end} ({page_count} page{'s' if page_count > 1 else ''}) in {cfg['sourceFile']}",
            'sourceFile': cfg['sourceFile']
        })
        print(f"  [EXTRACTED] {out_filename} (p. {p_start}-{p_end}, {file_size} bytes)")

manifest_path = os.path.join(BASE_DIR, 'data', 'intermediate', 'individual_pdfs_manifest.json')
with open(manifest_path, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, indent=2, ensure_ascii=False)

print(f"\nManifest successfully written to {manifest_path}")
print(f"Total Tamil individual PDFs: {len(manifest.get('Taml', []))}")
print(f"Total English individual PDFs: {len(manifest.get('Latn', []))}")
print(f"Total Telugu individual PDFs: {len(manifest.get('Telu', []))}")
