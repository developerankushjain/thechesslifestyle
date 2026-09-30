import os
import glob
import re

html_files = glob.glob('/Users/apple/Desktop/Projects/thechesslifestyle/**/*.html', recursive=True)

for file_path in html_files:
    if 'node_modules' in file_path or 'dist' in file_path or 'graphify-out' in file_path:
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    original_html = html
    
    # 1. Title Tag Optimization
    title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE | re.DOTALL)
    if title_match:
        current_title = title_match.group(1).strip()
        if len(current_title) > 60:
            if "Online Chess Classes in" in current_title:
                # Extract city
                match = re.search(r'Online Chess Classes in ([A-Za-z\s]+)', current_title)
                if match:
                    city = match.group(1).strip()
                    new_title = f"Online Chess Classes in {city} | Free 45-Min Trial"
                    if len(new_title) > 60:
                        new_title = f"Chess Classes in {city} | Free Trial"
                    html = html.replace(f"<title>{current_title}</title>", f"<title>{new_title}</title>")
            elif "TheChessLifestyle" in current_title:
                new_title = current_title.replace(" | TheChessLifestyle", "")
                if "—" in new_title:
                    new_title = new_title.split("—")[0].strip() + " | Free Trial"
                html = html.replace(f"<title>{current_title}</title>", f"<title>{new_title}</title>")

    # 2. Meta Description Optimization
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']\s*/?>', html, re.IGNORECASE | re.DOTALL)
    if not desc_match:
        # Inject missing meta description
        if "<head>" in html:
            new_desc = '<meta name="description" content="Learn chess from FIDE-rated masters. Tailored for kids and adults. Book your 100% free 45-minute trial class today!">'
            html = html.replace("<head>", f"<head>\n  {new_desc}")
    else:
        current_desc = desc_match.group(1)
        if "trial" not in current_desc.lower() and "free" not in current_desc.lower():
            new_desc = current_desc.strip()
            if not new_desc.endswith('.'):
                new_desc += '.'
            new_desc += ' Book your 100% free 45-minute trial today!'
            
            # Use regex sub to carefully replace the content
            html = re.sub(
                r'(<meta\s+name=["\']description["\']\s+content=["\'])(.*?)(["\']\s*/?>)', 
                r'\g<1>' + new_desc + r'\g<3>', 
                html, 
                flags=re.IGNORECASE | re.DOTALL
            )
            
            # also update og:description
            html = re.sub(
                r'(<meta\s+property=["\']og:description["\']\s+content=["\'])(.*?)(["\']\s*/?>)', 
                r'\g<1>' + new_desc + r'\g<3>', 
                html, 
                flags=re.IGNORECASE | re.DOTALL
            )

    if html != original_html:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Optimized CTR elements for: {file_path}")
