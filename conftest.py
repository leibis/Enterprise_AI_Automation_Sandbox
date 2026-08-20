import pytest
import time

# =====================================================================
# 🔌 FIXTURES GLOBALES DE CONEXIÓN (Nivel Enterprise)
# =====================================================================


@pytest.fixture(scope="session", autouse=True)
def inicio_sistema_qa():
    """
    Fixture de Alcance de Sesión (Session Scope).
    Se ejecuta UNA SOLA VEZ al iniciar toda la suite de pruebas.
    Simula el arranque de la infraestructura del CoE.
    """
    print(
        "\n\n🏁 [SYSTEM SETUP] Iniciando el entorno de pruebas automatizadas del CoE...")
    time.sleep(1)  # Simula el tiempo de arranque de la suite

    yield  # Aquí es donde se ejecutan los tests de todo tu proyecto

    print("\n🏁 [SYSTEM TEARDOWN] Suite de pruebas finalizada. Limpiando memoria y cerrando conexiones...")
