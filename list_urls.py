import os

base_url = "https://www.thechesslifestyle.com"
urls = []

for root, dirs, files in os.walk("."):
    # Ignore git or hidden directories
    if "/." in root:
        continue
    if root.startswith("./."):
        continue
            
    for file in files:
        if file.endswith(".html"):
            path = os.path.join(root, file)
            # Normalize path
            path = path.replace("\\", "/")
            if path.startswith("./"):
                path = path[2:]
            
            if path == "index.html":
                url = "/"
            elif path.endswith("/index.html"):
                url = "/" + path.replace("index.html", "")
            else:
                url = "/" + path
                
            urls.append(url)

urls.sort()
for url in urls:
    print(base_url + url)
