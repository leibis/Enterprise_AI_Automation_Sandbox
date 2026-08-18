# 🚀 Enterprise Cloud & AI Quality Gate - Test Automation Sandbox

[![GitHub Actions](https://github.com/leibis/Enterprise_AI_Automation_Sandbox/workflows/AAA%20Club%20Alliance%20-%20Automated%20QA%20Regression%20Suite/badge.svg)](https://github.com/leibis/Enterprise_AI_Automation_Sandbox/actions)
[![Coverage](https://img.shields.io/badge/coverage-79%25-brightgreen)](https://github.com/leibis/Enterprise_AI_Automation_Sandbox)
[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/pytest-9.1.1-orange)](https://pytest.org/)

## 📋 Project Description

This repository represents a hands-on, enterprise-grade test automation sandbox designed for a Cloud & Conversational AI ecosystem. It establishes a robust CI/CD Quality Gate that validates business logic, database integrations (GCP BigQuery), API endpoints, and critical Conversational AI safety guardrails (such as Prompt Injection and PII data masking).

## 🏗️ Framework Architecture
Enterprise_AI_Automation_Sandbox/
├── 🧪 tests/ # Automated Test Suites
│ ├── test_api_avanzado.py # REST APIs (POST, PUT, DELETE validations)
│ ├── test_api_reportes.py # Core endpoint validations
│ ├── test_bigquery_real.py # Google Cloud Platform database integration
│ ├── test_chatbot_ia.py # Conversational AI & response verification
│ ├── test_playwright_demo.py # Web E2E automation with Page Object Model
│ ├── test_secret_manager.py # Cloud secure credentials & injection
│ ├── test_seguridad_bola.py # OWASP API Security (BOLA protection)
│ └── test_seguridad_ia.py # AI Security (PII Masking & injection defense)
├── 📄 pages/ # Page Object Model (POM) Design Pattern
│ ├── PlaywrightDemoPage.py # Web Page Objects & selectors
│ └── chatbot_test.py # Chatbot automation components
├── ⚙️ .github/workflows/ # CI/CD Pipeline Configuration
│ └── run_tests.yml # Automated GitHub Actions Workflow
├── 📊 requirements.txt # Python dependencies
└── 🛡️ .gitignore # Security exclusions (ignores venv, credentials)



## 📊 Quality Metrics & Achievements

| Metric | Value | Status |
|---------|-------|--------|
| **Code Coverage** | 79% | ✅ Excellent |
| **Total Automated Tests** | 25 | ✅ Full Suite |
| **APIs Covered** | 8 | ✅ Functional |
| **OWASP Vulnerability Gates**| 0 Failures | ✅ Secure |
| **Execution Time** | < 7 seconds | ✅ Fast & Optimized |

## 🔧 Technologies Implemented

- **🐍 Python 3.12** - Core scripting language
- **🧪 Pytest** - Robust testing framework
- **🌐 Playwright** - Modern Web E2E UI testing
- **☁️ Google Cloud BigQuery** - Cloud data warehouse integration
- **🔒 GitHub Secrets & GCP Secret Manager** - Secure credential injection
- **⚡ GitHub Actions** - Cloud CI/CD automation runner
- **📊 Pytest-cov** - Dynamic code coverage analysis

## 🚀 Local Installation & Setup

### Prerequisites
- Python 3.12+
- Git Installed

### Local Setup
```bash
# Clone the repository
git clone https://github.com/leibis/Enterprise_AI_Automation_Sandbox.git
cd Enterprise_AI_Automation_Sandbox

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Install dependencies
pip install -r requirements.txt
playwright install chromium