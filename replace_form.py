import os
import glob

search_text = 'https://formspree.io/f/xvzjjenb'
replace_text = 'https://formspree.io/f/xvzjjenb'

honey_search = 'name="_gotcha"'
honey_replace = 'name="_gotcha"'

def replace_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if search_text in content or honey_search in content:
            content = content.replace(search_text, replace_text)
            content = content.replace(honey_search, honey_replace)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {filepath}")
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")

# Process all html, js, py files
extensions = ['**/*.html', '**/*.js', '**/*.py']
for ext in extensions:
    for filepath in glob.glob(ext, recursive=True):
        if 'node_modules' not in filepath and '.git' not in filepath:
            replace_in_file(filepath)

print("Done replacing.")
