import os
import re

replacements = {
    r'\bIndian FIDE Rated\b': 'International FIDE Rated',
    r'\bIndian FIDE Rated\b': 'International FIDE Rated',
    r'\bIndian FIDE\b': 'International FIDE',
    r'\bIndian coaches\b': 'international coaches',
    r'\bIndian Coaches\b': 'International Coaches',
    r'\bIndian Chess Coaches\b': 'International Chess Coaches',
    r'\bIndian FIDE Masters\b': 'International FIDE Masters',
    r'\bIndian instructors\b': 'international instructors',
    r'\bIndian Instructors\b': 'International Instructors',
    r'\bIndian chess coaches\b': 'international chess coaches'
}

target_dir = "."
count = 0

for root, dirs, files in os.walk(target_dir):
    if "node_modules" in root or ".git" in root or ".agent" in root:
        continue
    for file in files:
        if file.endswith(('.html', '.py', '.cjs', '.js', '.md', '.json', '.xml')):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                continue
            
            new_content = content
            for pattern, repl in replacements.items():
                new_content = re.sub(pattern, repl, new_content)
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
                count += 1

print(f"Total files updated: {count}")
