import os
import json
import random
import shutil
from datetime import datetime

SAMPLE_IMAGES_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../assets/sample_images'))
GENERATED_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../assets/generated'))
SAMPLE_IMAGES = [f for f in os.listdir(SAMPLE_IMAGES_DIR) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]

def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")

def generate_product_content():
    titles = [
        "sample_image1",
        "sample_image2",
        "sample_image3",
    ]
    descriptions = [
        "An Artificial intelligence image.",
        "A women holding thoughts in her mind",
        "AI driven technology.",
    ]
    tags_list = [
        ["Artificial", "intelligence", "image"],
        ["women", "thoughts", "mind"],
        ["AI", "driven", "technology"],
    ]
    idx = random.randint(0, len(titles) - 1)
    return {
        "title": titles[idx],
        "description": descriptions[idx],
        "tags": tags_list[idx]
    }

def simulate_image_generation():
    if not SAMPLE_IMAGES:
        raise FileNotFoundError("No sample images found in assets/sample_images/")
    chosen = random.choice(SAMPLE_IMAGES)
    src = os.path.join(SAMPLE_IMAGES_DIR, chosen)
    dest = os.path.join(GENERATED_DIR, f"product_image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png")
    shutil.copyfile(src, dest)
    return dest

def save_product_json(product, image_path):
    output = {
        "title": product["title"],
        "description": product["description"],
        "tags": product["tags"],
        "image_path": image_path,
        "timestamp": datetime.now().isoformat()
    }
    out_path = os.path.join(GENERATED_DIR, "product.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
    return out_path

def main():
    log("Starting Product Content Generator...")
    try:
        product = generate_product_content()
        log(f"Generated product: {product['title']}")
        image_path = simulate_image_generation()
        log(f"Simulated image generation: {os.path.basename(image_path)}")
        out_json = save_product_json(product, image_path)
        log(f"Saved product data to {out_json}")
    except Exception as e:
        log(f"ERROR: {e}")

if __name__ == "__main__":
    main()