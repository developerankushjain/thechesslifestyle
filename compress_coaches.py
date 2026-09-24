import os, subprocess

coach_dir = "coaches"
images = [f for f in os.listdir(coach_dir) if f.endswith('.png') or f.endswith('.jpg')]

for img in images:
    src = os.path.join(coach_dir, img)
    base = os.path.splitext(img)[0]
    dst = os.path.join(coach_dir, base + ".webp")
    
    before = os.path.getsize(src)
    # cwebp with quality 80, resize width to max 600px
    result = subprocess.run(
        ["cwebp", "-q", "80", "-resize", "600", "0", src, "-o", dst],
        capture_output=True, text=True
    )
    if result.returncode == 0:
        after = os.path.getsize(dst)
        saving = (1 - after/before) * 100
        print(f"✅ {img}: {before//1024}KB → {after//1024}KB ({saving:.0f}% saved)")
    else:
        print(f"❌ {img} failed: {result.stderr}")

print("\nDone! Now update HTML references from .png/.jpg → .webp")
