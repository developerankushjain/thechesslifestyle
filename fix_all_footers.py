import os
import re

target_dir = "."
pattern = re.compile(r'<div class="footer-col contact-info">
        <h3>Contact Us</h3>
        <p>📍 Global Online Operations</p>
        <a href="mailto:admin@thechesslifestyle.com">admin@thechesslifestyle.com</a>
      </div>', re.DOTALL)
replacement = '''<div class="footer-col contact-info">
        <h3>Contact Us</h3>
        <p>📍 Global Online Operations</p>
        <a href="mailto:admin@thechesslifestyle.com">admin@thechesslifestyle.com</a>
      </div>'''

count = 0
for root, dirs, files in os.walk(target_dir):
    if "node_modules" in root or ".git" in root or ".agent" in root:
        continue
    for file in files:
        if file.endswith(('.html', '.py', '.cjs', '.js')):
            filepath = os.path.join(root, file)
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = pattern.sub(replacement, content)
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")
                count += 1

print(f"Total files updated: {count}")
