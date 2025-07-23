
# Project Architecture & Problem-Solving Approach

The **AI Merch Maker Lite** project is built around the idea of simulating a real-world automated pipeline using four different programming languages — each performing a core function in the product listing lifecycle. Here's how the architecture is designed:

---

#  System Architecture Diagram

```
+---------------------+
|  Task 1: Python     |
|  Product Generator  |
|  (AI-Simulated)     |
+----------+----------+
           |
           v
+------------------------+
| Task 2: HTML + JS      |
| Mock Product Visualizer|
| (Canvas + JSON Output) |
+----------+-------------+
           |
           v
+---------------------+
|  Task 3: PHP Server |
|  Fake Publisher     |
|  (Accepts POST JSON)|
+----------+----------+
           |
           v
+---------------------------+
| Task 4: Python Orchestrator|
| (End-to-End Automation)    |
+---------------------------+
```

---

#  Problem-Solving Approach

# 1. Language Allocation
Each task was assigned a language best suited for it:
- **Python** for logic, file handling, and automation
- **HTML/JS** for interactive product mockup simulation
- **PHP** for simulating backend publishing APIs

# 2. Task Isolation & Modularity
Tasks were built modularly and independently to allow testing each module on its own, then integrated together using Python's `subprocess` and API calls.

# 3. Automation First
The orchestrator script acts as a control tower — triggering all tasks and ensuring clean logs, error handling, and integration between modules.

# 4. AI Simulation for Cost-Free Execution
Instead of live OpenAI API calls (which are paid), simulated AI logic (using randomization, structured data, base64 encoding) was used to mimic realistic product generation — making it fully executable without cloud cost.

# 5. Developer-Style Structure
The code is structured with:
- Folder separation by language (`/python`, `/php`, `/js`, `/assets`)
- CLI-style logs in Python
- REST-like API interaction in PHP
- Interactive and responsive UI

# 6. Bonus Layer
- HTML canvas is made beautiful and branded
- All outputs are visual and exportable (JSON, images)
- PHP logs simulate real-world endpoints and IDs

---

# Execution Principles Followed

| Principle            | Description |
|----------------------|-------------|
| Modular Coding       | Each file does one job only |
| Language Strengths   | Chosen per task type |
| Reusability          | Task 1 data is reused in Task 2 & 3 |
| Testability          | Every component runs independently |
| User-Friendliness    | UI is clear, buttons are self-explanatory |
| Clarity              | README and scripts are well-commented |
