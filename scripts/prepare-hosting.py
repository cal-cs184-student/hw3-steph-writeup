#!/usr/bin/env python3
"""Stage this report in a personal-site checkout; no commits or pushes."""
from pathlib import Path
import argparse, shutil
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('website', type=Path, help='Checkout of suniyao/suniyao.github.io')
p.add_argument('--activate-redirect', action='store_true', help='Only after the personal-site page is live: replace the course index with its redirect')
a=p.parse_args()
root=Path(__file__).resolve().parents[1]
site=a.website.resolve()
if not (site/'next.config.ts').is_file() or not (site/'public').is_dir():
 p.error('Expected the personal website checkout with next.config.ts and public/.')
source=root/'index.html'
if 'http-equiv="refresh"' in source.read_text():source=root/'report.html'
if not source.is_file():p.error('The source report could not be found.')
target=site/'public/cs184/hw3'
target.mkdir(parents=True,exist_ok=True)
shutil.copy2(source,target/'index.html')
shutil.copy2(root/'report.css',target/'report.css')
shutil.copy2(root/'math.js',target/'math.js')
shutil.copytree(root/'assets',target/'assets',dirs_exist_ok=True)
if a.activate_redirect:
 shutil.copy2(source,root/'report.html') if source != root/'report.html' else None
 shutil.copy2(root/'redirect.html',root/'index.html')
print('Staged:',target)
print('No commits, pushes, or deployments were performed.')
