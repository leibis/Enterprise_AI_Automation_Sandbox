# 🚀 AAA Club Alliance - Automated QA Regression Suite

[![GitHub Actions](https://github.com/leibis/AAA_Automation_Suite/workflows/AAA%20Club%20Alliance%20-%20Automated%20QA%20Regression%20Suite/badge.svg)](https://github.com/leibis/AAA_Automation_Suite/actions)
[![Coverage](https://img.shields.io/badge/coverage-79%25-brightgreen)](https://github.com/leibis/AAA_Automation_Suite)
[![Python](https://img.shields.io/badge/python-3.12-blue)](https://www.python.org/)
[![Pytest](https://img.shields.io/badge/pytest-9.1.1-orange)](https://pytest.org/)

## 📋 Descripción del Proyecto

Framework de automatización de pruebas de regresión completo para el Centro de Excelencia (CoE) de AAA Club Alliance. Implementa las mejores prácticas de ingeniería de calidad con arquitectura de microservicios, seguridad avanzada y CI/CD.

## 🏗️ Arquitectura del Framework

AAA_Automation_Suite/
├── 🧪 tests/ # Suite de Pruebas Automatizadas
│ ├── test_api_avanzado.py # APIs REST (POST, PUT, DELETE)
│ ├── test_api_reportes.py # Validación de endpoints
│ ├── test_bigquery_real.py # Integración con Google Cloud
│ ├── test_chatbot_ia.py # Pruebas de IA convers
acional
│ ├── test_playwright_demo.py # Automatización web E2E
│ ├── test_secret_manager.py # Seguridad de credenciales
│ ├── test_seguridad_bola.py # Vulnerabilidades OWASP
│ └── test_seguridad_ia.py # Ciberseguridad avanzada
├── 📄 pages/ # Page Object Model (POM)
│ ├── PlaywrightDemoPage.py # Objetos de página web
│ └── chatbot_test.py # Componentes de chatbot
├── ⚙️ .github/workflows/ # Pipeline CI/CD
│ └── run_tests.yml # GitHub Actions automatizado
├── 📊 requirements.txt # Dependencias del proyecto
└── 🛡️ .gitignore # Configuración de seguridad

## 📊 Métricas de Calidad

| Métrica | Valor | Estado |
|---------|-------|--------|
| **Cobertura de Código** | 79% | ✅ Excelente |
| **Tests Automatizados** | 25 | ✅ Completo |
| **APIs Validadas** | 8 | ✅ Funcional |
| **Vulnerabilidades OWASP** | 0 | ✅ Seguro |
| **Tiempo de Ejecución** | <7s | ✅ Rápido |

## 🔧 Tecnologías Implementadas

- **🐍 Python 3.12** - Lenguaje principal
- **🧪 Pytest** - Framework de testing
- **🌐 Playwright** - Automatización web E2E
- **☁️ Google Cloud BigQuery** - Base de datos en la nube
- **🔒 GitHub Secrets** - Gestión segura de credenciales
- **⚡ GitHub Actions** - CI/CD automatizado
- **📊 Pytest-cov** - Análisis de cobertura

## 🚀 Instalación y Configuración

### Prerrequisitos
- Python 3.12+
- Git
- Cuenta de GitHub

### Instalación Local
```bash
# Clonar el repositorio
git clone https://github.com/leibis/AAA_Automation_Suite.git
cd AAA_Automation_Suite

# Crear entorno virtual
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# Instalar dependencias
pip install -r requirements.txt
playwright install chromium

🛡️ Características de Seguridad
✅ Implementadas
Inyección de Secretos: Credenciales encriptadas en GitHub
Validación OWASP: Prevención de vulnerabilidades BOLA
Prompt Injection Protection: Seguridad en IA conversacional
Masking de Datos Sensibles: Protección de tarjetas de crédito
Autenticación Segura: Validación de tokens de acceso



Ejecución de Pruebas
# Ejecutar suite completa
pytest -v -s

# Ejecutar con cobertura
pytest --cov=. --cov-report=term-missing -v

# Ejecutar pruebas específicas
pytest tests/test_seguridad_ia.py -v



🔒 Configuración de Secretos
# GitHub Repository Secrets
GCP_CREDENTIALS_JSON: {"type": "service_account", "project_id": "..."}


📈 Pipeline CI/CD
El pipeline se ejecuta automáticamente en cada push:

🔄 Checkout - Descarga el código
🐍 Setup Python - Configura el entorno
📦 Install Dependencies - Instala librerías
🧪 Run Tests - Ejecuta 25 pruebas automatizadas
📊 Coverage Report - Genera métricas de cobertura
🎯 Casos de Uso Validados
✅ APIs REST: CRUD completo con validaciones
✅ Seguridad: Prevención de
ataques OWASP
✅ Big Data: Consultas a Google Cloud BigQuery
✅ IA Conversacional: Chatbot con protecciones
✅ Automatización Web: Flujos E2E con Playwright
✅ DevOps: Pipeline completamente automatizado


👩‍💻 Desarrollado por
Leidy Reyes - QA Lead/Staff Engineer

Framework desarrollado siguiendo las mejores prácticas de ingeniería de calidad para entornos empresariales de alto rendimiento.