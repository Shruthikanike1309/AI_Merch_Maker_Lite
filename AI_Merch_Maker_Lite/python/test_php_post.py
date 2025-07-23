import requests
import json

data = {
  "title": "Test Product",
  "description": "Sample",
  "tags": ["sample", "test"]
}

# Since you're running from inside the php/ folder:
resp = requests.post("http://localhost:8000/fake_product_publisher.php", json=data)

print(resp.status_code)
print(resp.text)
