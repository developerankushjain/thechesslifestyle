import os
import subprocess

for root_dir in ['gallery', 'coaches']:
    if not os.path.exists(root_dir):
        continue
    for f in os.listdir(root_dir):
        if f.lower().endswith(('.jpg', '.jpeg', '.png')):
            filepath = os.path.join(root_dir, f)
            subprocess.run(['sips', '-Z', '1280', '-s', 'formatOptions', '70', filepath, '--out', filepath])

print("Compression complete!")
