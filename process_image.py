from PIL import Image, ImageEnhance
import os

input_path = 'coaches/Prem.jpeg'
output_path = 'coaches/Prem.webp'

if os.path.exists(input_path):
    # Open the image
    img = Image.open(input_path)
    
    # Enhance brightness (1.0 is original, 1.2 is 20% brighter)
    enhancer = ImageEnhance.Brightness(img)
    img_bright = enhancer.enhance(1.2)
    
    # Convert and save as WebP with optimized quality
    img_bright.save(output_path, 'WEBP', quality=80, method=6)
    print("Image brightened and converted to webp successfully.")
else:
    print("Input image not found.")
