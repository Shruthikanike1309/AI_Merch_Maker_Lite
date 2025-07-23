# Orchestrator Usage Guide

1. Start the PHP server in the project root (where the php/ folder is):

   php -S localhost:8000

2. Make sure Node.js is installed and available in your PATH.

3. From the python/ directory, run:

   python orchestrator.py

This will:
- Generate a product (Python)
- Create a mockup (Node.js)
- Send the mockup to the PHP endpoint

Check the sample_output/ folder for intermediate results and the terminal for the final response.
