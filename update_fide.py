import re

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if '<div class="fide-badge">FIDE ID: 25971115</div>' in content:
        content = content.replace('<div class="fide-badge">FIDE ID: 25971115</div>', '<div class="fide-badge">FIDE ID: 25971115 &nbsp;|&nbsp; Peak FIDE Rating: 1729</div>')
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

update_file('index.html')
update_file('online-chess-classes-usa/index.html')

with open('generate-pages.js', 'r', encoding='utf-8') as f:
    js_content = f.read()

if 'FIDE ID: <a href' in js_content:
    pass # Needs manual check

