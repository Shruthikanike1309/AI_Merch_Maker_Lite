import os
import sys
import subprocess
import json
import requests
from datetime import datetime
def log(msg):
    print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {msg}")
ROOT = os.path.abspath(os.path.dirname(__file__))
PRODUCT_GEN_SCRIPT = os.path.join(ROOT, 'product_generator.py')  #paths of the project
PRODUCT_JSON = os.path.abspath(os.path.join(ROOT, 'assets', 'generated', 'product.json'))
PHP_ENDPOINT = 'http://localhost:8000/php/fake_product_publisher.php'
def run_product_generator():
    log("▶Running Task 1: Product Generator...")
    subprocess.run([sys.executable, PRODUCT_GEN_SCRIPT], check=True)
def send_to_php():
    log("Sending product.json to Task 3 (PHP publisher)...")
    if not os.path.exists(PRODUCT_JSON):
        log("product.json found.")
        return
    with open(PRODUCT_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    try:
        resp = requests.post(PHP_ENDPOINT, json=data)
        log(f"PHP Response: {resp.text}")
    except Exception as e:
        log(f"Failed to send to PHP: {e}")

def main():
    try:
        run_product_generator()
        log("(Task 2 is visual, open manually if needed)")
        send_to_php()
        log("Task 4 Automation Complete!")
    except Exception as e:
        log(f"ERROR in automation: {e}")
if __name__ == "__main__":
    main()
