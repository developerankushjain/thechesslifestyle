import os
import re

alt_tag_html = '<meta property="og:image:alt" content="TheChessLifestyle — Online Chess Classes by FIDE Rated Coaches">'
alt_tag_html_slash = '<meta property="og:image:alt" content="TheChessLifestyle — Online Chess Classes by FIDE Rated Coaches" />'

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    if 'og:image:alt' in content:
        return # already added

    original_content = content
    if filepath.endswith('.html'):
        # insert after og:image or og:image:height
        if '<meta property="og:image:height"' in content:
            content = re.sub(r'(<meta property="og:image:height"[^>]*>)', r'\1\n    ' + alt_tag_html_slash, content)
        elif '<meta property="og:image"' in content:
             content = re.sub(r'(<meta property="og:image"[^>]*>)', r'\1\n    ' + alt_tag_html_slash, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")

for root, dirs, files in os.walk('.'):
    if 'node_modules' in dirs: dirs.remove('node_modules')
    if '.git' in dirs: dirs.remove('.git')
    for file in files:
        if file.endswith('.html'):
            process_file(os.path.join(root, file))
