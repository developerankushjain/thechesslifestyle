import os
import re

target_dir = "."
count = 0

email_pattern = re.compile(r'hello@thechesslifestyle\.com', re.IGNORECASE)
wa_link_pattern = re.compile(r'<a[^>]*href="https://wa\.me/[^>]*>.*?</a>', re.DOTALL | re.IGNORECASE)

for root, dirs, files in os.walk(target_dir):
    if "node_modules" in root or ".git" in root or ".agent" in root:
        continue
    for file in files:
        if file.endswith(('.html', '.py', '.cjs', '.js', '.md')):
            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
            except UnicodeDecodeError:
                continue
            
            new_content = email_pattern.sub('admin@thechesslifestyle.com', content)
            new_content = wa_link_pattern.sub('', new_content)
            new_content = new_content.replace('Phone', 'Phone')
            new_content = new_content.replace('Phone', 'Phone')
            new_content = new_content.replace('', '')
            new_content = new_content.replace('', '')
            
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1

print(f"Total files updated: {count}")
