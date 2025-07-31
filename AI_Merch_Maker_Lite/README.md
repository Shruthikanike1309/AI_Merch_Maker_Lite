
# AI Merch Maker Lite (Simulation)

A modular, fully simulated pipeline for automated AI-generated product listings, using Python, JavaScript (Node.js), and PHP. No real AI APIs are used—everything is simulated for a real-world developer experience.

## Project Structure

```
assets/
  sample_images/      # Place sample images here (e.g., sample1.png)
  generated/          # All generated outputs (product.json, mockup.json, preview images, logs)
js/
  mock_product_visualizer.js
php/
  fake_product_publisher.php
python/
  product_generator.py
  orchestrator.py
```

## How It Works

1. **Product Content Generator (Python)**
   - Generates a random product (title, description, tags)
   - Simulates image generation by copying a sample image
   - Saves output as `assets/generated/product.json`

2. **Mock Product Visualizer (Node.js)**
   - Loads the generated product image
   - Overlays it on a T-shirt mockup using Canvas
   - Outputs a mockup preview image and `mockup.json` in `assets/generated/`

3. **Fake Product Publisher (PHP)**
   - Simple endpoint at `/php/fake_product_publisher.php`
   - Accepts POSTed JSON, logs it, returns a simulated product ID

4. **Automation Orchestrator (Python)**
   - Runs the above steps in order
   - Logs each step with timestamps
   - Ready for daily automation (e.g., via cron or Task Scheduler)

## Quick Start

1. Place at least one image in `assets/sample_images/` (e.g., `sample1.png`).
2. Start the PHP server in the project root:
   ```
   php -S localhost:8000
   ```
3. Run the orchestrator:
   ```
   cd ../python
   python orchestrator.py
   ```

## Output
- All generated files and logs are in `assets/generated/`
- Outputs of the terminal and the final product ID are in documentation.

---

**This project is a simulation for learning purposes. No real AI or eCommerce APIs are used.**
