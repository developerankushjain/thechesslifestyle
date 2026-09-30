import os
import glob

html_files = glob.glob('/Users/apple/Desktop/Projects/thechesslifestyle/**/*.html', recursive=True)

old_str = '<form action="https://formspree.io/f/xvzjjenb" method="POST">'
new_str = '<form action="https://formspree.io/f/xvzjjenb" method="POST" onsubmit="const b = this.querySelector(\'button[type=submit]\'); b.innerHTML = \'Booking...\'; b.style.opacity = \'0.7\'; b.style.cursor = \'wait\';">'

# Note: I am intentionally NOT disabling the button (b.disabled = true) because some browsers/formspree 
# might abort the native form submission if the submit button becomes disabled during the submit event.
# Changing text and cursor is safer for native form submissions.

for file in html_files:
    if 'node_modules' in file:
        continue
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    if old_str in content:
        content = content.replace(old_str, new_str)
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file}")
