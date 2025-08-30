# 🛡️ DevSecOps CI/CD Pipeline

This project demonstrates a secure CI/CD pipeline using GitHub Actions, including security testing, secrets detection, and Docker image scanning.

## 💡 Features

- Flask API with testable routes
- GitHub Actions CI/CD pipeline
- Bandit for Python static security scanning
- Gitleaks for secrets detection
- Trivy for Docker image vulnerability scanning
- Pytest for basic testing

## 📁 Project Structure
.
├── app/
├── test/
├── .env
├── .gitleaks.toml
├── Dockerfile
└── .github/workflows/ci-cd.yml

## 🚀 Getting Started
### 🔧 Local Run

```bash
pip install -r app/requirements.txt
python app/main.py

```

### RUN TESTS
pytest

### Docker
docker build -t devsecops-api .

docker run -p 5000:5000 devsecops-api

----
## RUN TESTS:
<img width="1824" height="709" alt="image" src="https://github.com/user-attachments/assets/de415bbe-55c0-479b-a3fd-1915d4803e97" />

## Bandit scan
<img width="1827" height="916" alt="image" src="https://github.com/user-attachments/assets/7fa50dbb-3d6f-404b-b7de-e3d266cda849" />

## gitleaks Scan
<img width="1847" height="900" alt="image" src="https://github.com/user-attachments/assets/9b15c3a6-b09e-4075-a2af-02d476640fdc" />

## Docker image with trivy scan
<img width="1825" height="926" alt="image" src="https://github.com/user-attachments/assets/c047eedb-855e-455f-bcf3-826d77dc796c" />

<img width="1826" height="923" alt="image" src="https://github.com/user-attachments/assets/4a813628-41c9-4c22-902a-72ec473eb2d8" />

---

# THANK YOU

## Common Pytest Error in CI Pipelines

📌 Error Summary:
ImportError while importing test module '.../test/test_main.py'.
**ModuleNotFoundError: No module named 'app'**

🛠️ Root Cause
Your test file is trying to import:
from app.main import app
But the module app is not found in the** Python path **during the test run. 

✅ Common Causes and Fixes
1. Module Not in PYTHONPATH
Cause: The app directory is not in the PYTHONPATH during test execution.
Fix: Add the root directory to PYTHONPATH in your workflow:

- name: Run tests
  run: |
**    PYTHONPATH=. pytest**

💡 Best Practice Tips
Ensure the directory structure is clean and consistent.
Always test locally using the same command you're running in CI.
Add logging or print sys.path in your test to debug module paths if needed:
import sys; print(sys.path)

## Common Security Errors Found by Bandit

🔍 Bandit Results Summary
Issue	Severity	Confidence	Line	Description
B602	High	High	Line 39	subprocess with shell=True — Command injection risk
B201	High	Medium	Line 44	Flask running with debug=True — Exposes internal debugger
B104	Medium	Medium	Line 44	Binds to all interfaces (0.0.0.0) — Security risk in prod

📊 Summary of Bandit Scan
Severity	Issues
High	2
Medium	1
Low	1

**✅ What This Means
Your pipeline is working correctly — it’s catching vulnerabilities. Now, you have two paths depending on your intent:**

🎯 OPTION 1: Keep the Issues for Learning
Goal: Show a real pipeline catching vulnerabilities.

✅ You do not need to fix the code.
These vulnerabilities are intentionally left to demonstrate how Bandit detects them.

The pipeline fails by design when issues are present.

📝 Example:

### ❗ Known Security Issues (Intended)
- `subprocess` with `shell=True`: simulates command injection (caught by Bandit)
- `debug=True` in Flask: intentionally insecure for testing
- Binding to `0.0.0.0`: to simulate prod misconfigurations

Bandit flags these to demonstrate pipeline effectiveness.

Then in GitHub Actions:

# Optional: allow pipeline to continue even if Bandit fails
- name: Run Bandit (non-blocking demo)
  run: |
**    bandit -r app/ -ll || true**


🔐 OPTION 2: Fix the Vulnerabilities for Production Readiness

If you're ready to "harden" the app, here's how to fix each:

🔧 Fix B602: subprocess with shell=True
# BAD
output = subprocess.check_output(cmd, shell=True)

# BETTER (safe example)
import shlex
output = subprocess.check_output(shlex.split(cmd))


✅ Avoid shell=True when possible, or whitelist commands explicitly.
🔧 Fix B201: debug=True in Production

Change this:
app.run(debug=True, host='0.0.0.0', port=port)

To:
debug = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
app.run(debug=debug, host='127.0.0.1', port=port)

And in .env, set:
FLASK_DEBUG=false

✅ Use env variables for config (12-factor style).
🔧 Fix B104: Binding to all interfaces
Use 127.0.0.1 or limit access via a reverse proxy (like Nginx).


🧾 Suggested Remediation Steps
Refactor subprocess usage to remove shell=True or validate input.
Disable Flask debug mode in production environments.
Restrict binding to 127.0.0.1, unless public access is explicitly required and secured.
Use environment variables to toggle debug settings securely.


---

### Common Gitleaks Errors (Security Scanning Context)

❗ Problem Summary
1. Gitleaks Config Error

Failed to load config error="rule |id| is missing or empty"

Your .gitleaks.toml has custom rules without id fields, which is now mandatory in Gitleaks v8+.

✅ Fix #1: Add Required id Fields in .gitleaks.toml

Update your .gitleaks.toml to include unique id fields for each rule.

# Thank you



