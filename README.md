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

### RUN TESTS
pytest

### Docker
docker build -t devsecops-api .
docker run -p 5000:5000 devsecops-api

----
##RUN TESTS:
<img width="1824" height="709" alt="image" src="https://github.com/user-attachments/assets/de415bbe-55c0-479b-a3fd-1915d4803e97" />

##Bandit scan
<img width="1827" height="916" alt="image" src="https://github.com/user-attachments/assets/7fa50dbb-3d6f-404b-b7de-e3d266cda849" />

##gitleaks Scan
<img width="1847" height="900" alt="image" src="https://github.com/user-attachments/assets/9b15c3a6-b09e-4075-a2af-02d476640fdc" />

##Docker image with trivy scan
<img width="1825" height="926" alt="image" src="https://github.com/user-attachments/assets/c047eedb-855e-455f-bcf3-826d77dc796c" />

<img width="1826" height="923" alt="image" src="https://github.com/user-attachments/assets/4a813628-41c9-4c22-902a-72ec473eb2d8" />

