import os
import re

new_logo = '''<a href="/" class="logo">
        <img src="/favicon.svg" alt="TheChessLifestyle Chess King Logo" class="logo-icon" width="32" height="35" loading="eager"/>
        TheChessLifestyle
      </a>'''

# Regex to find <nav class="navbar"> followed by either <div class="logo">...</div> or <a href="/" class="logo">...</a>
# We'll use a non-greedy match for the logo block.
logo_pattern = re.compile(
    r'(<nav class="navbar">\s*)(?:<div class="logo">.*?</div>|<a href="/" class="logo">.*?</a>)', 
    re.DOTALL
)

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content, count = logo_pattern.subn(r'\1' + new_logo, content)
    
    if count > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated logo in {filepath}")

for root, dirs, files in os.walk('.'):
    # Skip build/dependency dirs
    if any(skip in root for skip in ['node_modules', 'dist', '.git', '.venv']):
        continue
    
    for file in files:
        if file.endswith('.html') or file in ['generate-cities.py', 'generate-pages.py', 'generate-pages.js']:
            process_file(os.path.join(root, file))
