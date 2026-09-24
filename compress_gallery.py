import os, subprocess

gallery_dir = "gallery"
images = [f for f in os.listdir(gallery_dir) if f.lower().endswith('.jpg') or f.lower().endswith('.jpeg')]

total_before = 0
total_after = 0

for img in images:
    src = os.path.join(gallery_dir, img)
    base = os.path.splitext(img)[0]
    dst = os.path.join(gallery_dir, base + ".webp")
    
    before = os.path.getsize(src)
    total_before += before
    result = subprocess.run(
        ["cwebp", "-q", "75", src, "-o", dst],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        after = os.path.getsize(dst)
        total_after += after
        saving = (1 - after/before) * 100
        print(f"✅ {img}: {before//1024}KB → {after//1024}KB ({saving:.0f}% saved)")
    else:
        print(f"❌ {img} failed")

print(f"\nTotal: {total_before//1024}KB → {total_after//1024}KB ({(1-total_after/total_before)*100:.0f}% saved)")
