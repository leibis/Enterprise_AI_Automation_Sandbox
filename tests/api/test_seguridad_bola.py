import pytest

# =====================================================================
# 🤖 SIMULADOR DE API DE LA AAA CON FILTRO DE AUTORIZACIÓN (BACKEND)
# =====================================================================

# Simulamos los datos confidenciales de los socios en BigQuery
BASE_DATOS_CONFIDENCIAL = {
    "SOCIO-007": {"nombre": "James Bond", "tarjeta": "4532-XXXX-XXXX-1234"},
    "SOCIO-008": {"nombre": "Sherlock Holmes", "tarjeta": "5412-XXXX-XXXX-5678"}
}


def consultar_datos_socio_api(id_solicitante: str, id_objetivo: str) -> dict:
    """
    Simula una API de reportes que valida la identidad del solicitante antes
    de mostrar los datos confidenciales del id_objetivo.
    """
    # 🛡️ FILTRO DE SEGURIDAD (Prevención de vulnerabilidad BOLA)
    # Validamos que el socio que solicita los datos SEA el dueño de la información
    if id_solicitante != id_objetivo:
        return {
            # 403 significa "Forbidden" (Acceso Prohibido por seguridad)
            "status_code": 403,
            "error": "ACCESO DENEGADO: No tienes autorización para ver los datos de este socio."
        }

    # Si pasa el filtro de seguridad, devolvemos los datos de BigQuery
    datos = BASE_DATOS_CONFIDENCIAL[id_objetivo]
    return {
        "status_code": 200,
        "id_socio": id_objetivo,
        "nombre": datos["nombre"],
        "tarjeta_enmascarada": datos["tarjeta"]
    }


# =====================================================================
# 🧪 SUITE DE PRUEBAS DE CIBERSEGURIDAD DE APIs CON PYTEST
# =====================================================================

# Prueba 1: Acceso Autorizado (Camino Feliz)
def test_acceso_autorizado_propios_datos():
    print(
        "\n[Security QA] Verificando que un socio pueda consultar sus propios datos...")

    # El SOCIO-007 solicita sus propios datos (SOCIO-007)
    respuesta = consultar_datos_socio_api(
        id_solicitante="SOCIO-007", id_objetivo="SOCIO-007")

    assert respuesta["status_code"] == 200
    assert respuesta["nombre"] == "James Bond"


# Prueba 2: Intento de Vulnerabilidad BOLA (Debe ser bloqueado por la API)
def test_seguridad_prevencion_vulnerabilidad_bola():
    print("\n[Security QA] Intentando hackear la API para ver datos de otro socio (BOLA)...")

    # El SOCIO-007 (James Bond) intenta consultar de forma maliciosa los datos de SOCIO-008 (Sherlock)
    respuesta = consultar_datos_socio_api(
        id_solicitante="SOCIO-007", id_objetivo="SOCIO-008")

    # 🎯 VALIDACIÓN DE SEGURIDAD (Aserción)
    # Afirmamos que la API DEBE bloquear la petición con un código 403 (Acceso Prohibido)
    assert respuesta["status_code"] == 403, "CRÍTICO: La API permitió a un usuario ver datos de otro socio."
    assert "ACCESO DENEGADO" in respuesta["error"]
