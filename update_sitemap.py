import os
import xml.etree.ElementTree as ET
from datetime import datetime

sitemap_path = 'public/sitemap.xml'
if not os.path.exists(sitemap_path):
    print("No sitemap found!")
    exit(1)

tree = ET.parse(sitemap_path)
root = tree.getroot()

ns = {'sitemap': 'http://www.sitemaps.org/schemas/sitemap/0.9'}
ET.register_namespace('', ns['sitemap'])

# Track existing URLs
existing_urls = []
for url in root.findall('sitemap:url', ns):
    loc = url.find('sitemap:loc', ns)
    if loc is not None:
        url_text = loc.text
        existing_urls.append(url_text)
        
        # Determine actual file modification date
        # Map URL to local path
        path = url_text.replace('https://www.thechesslifestyle.com/', '')
        if path == '' or path == '/':
            local_path = 'index.html'
        else:
            local_path = os.path.join(path, 'index.html')
            
        if os.path.exists(local_path):
            mtime = os.path.getmtime(local_path)
            lastmod_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
            
            lastmod = url.find('sitemap:lastmod', ns)
            if lastmod is not None:
                lastmod.text = lastmod_str

# Add missing US cities
us_cities = [
    'online-chess-classes-new-york',
    'online-chess-classes-los-angeles',
    'online-chess-classes-chicago',
    'online-chess-classes-houston'
]

for city in us_cities:
    url_text = f"https://www.thechesslifestyle.com/{city}/"
    if url_text not in existing_urls:
        url_elem = ET.SubElement(root, 'url')
        
        loc_elem = ET.SubElement(url_elem, 'loc')
        loc_elem.text = url_text
        
        local_path = os.path.join(city, 'index.html')
        lastmod_str = datetime.now().strftime('%Y-%m-%d')
        if os.path.exists(local_path):
            mtime = os.path.getmtime(local_path)
            lastmod_str = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d')
            
        lastmod_elem = ET.SubElement(url_elem, 'lastmod')
        lastmod_elem.text = lastmod_str
        
        changefreq = ET.SubElement(url_elem, 'changefreq')
        changefreq.text = 'monthly'
        
        priority = ET.SubElement(url_elem, 'priority')
        priority.text = '0.8'

tree.write(sitemap_path, encoding='utf-8', xml_declaration=True)
print("Sitemap updated successfully!")
