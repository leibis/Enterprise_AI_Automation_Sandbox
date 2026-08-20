import pytest
from unittest.mock import MagicMock

# =====================================================================
# 🤖 SIMULADOR DE LA API DE REPORTES DE LA AAA (BACKEND)
# =====================================================================


def obtener_reporte_servicios_api(region):
    # En la vida real, esta función haría una petición HTTP real a:
    # f"https://api.aaa.com/v1/reports?region={region}"
    # Y consultaría los datos reales de BigQuery.

    # Simulamos la respuesta JSON estándar que devolvería el mesero (API)
    if region == "NORTHEAST":
        return {
            "status_code": 200,
            "region": "NORTHEAST",
            "total_servicios_completados": 1450,
            "tiempo_espera_promedio_minutos": 24.5,
            "servicios_fallidos": 0,
            "datos_sensibles_expuestos": False
        }
    else:
        return {
            "status_code": 404,
            "error": "Región no encontrada o sin datos disponibles."
        }


# =====================================================================
# 🧪 SUITE DE PRUEBAS DE API DE REPORTES CON PYTEST (TU ROL DE QA)
# =====================================================================

# Prueba 1: Verificar el reporte exitoso para la región NORTHEAST
def test_api_reporte_exitoso():
    # 1. Ejecutamos la llamada a la API simulada
    respuesta = obtener_reporte_servicios_api("NORTHEAST")

    # 2. Hacemos las validaciones de QA (Aserciones de API)
    assert respuesta["status_code"] == 200, "Error: La API debería responder con estado 200 OK."
    assert respuesta["region"] == "NORTHEAST"

    # Validamos que el tiempo de espera promedio sea un número lógico (mayor a cero)
    assert respuesta["tiempo_espera_promedio_minutos"] > 0
    assert respuesta["tiempo_espera_promedio_minutos"] < 60, "Alerta: El tiempo de espera promedio supera el límite de servicio de 1 hora."


# Prueba 2: Validar el manejo de errores de la API (Región inexistente)
def test_api_reporte_no_encontrado():
    respuesta = obtener_reporte_servicios_api("REGIO_FANTASMA")

    # Validamos que la API responda correctamente con un error de cliente 404
    assert respuesta["status_code"] == 404
    assert "error" in respuesta


# Prueba 3: Regla de Oro de Seguridad - Cero fugas de datos confidenciales en los reportes
def test_api_reporte_seguridad_datos():
    respuesta = obtener_reporte_servicios_api("NORTHEAST")

    # Aseguramos que la API tenga activo el filtro de seguridad de datos sensibles
    assert respuesta["datos_sensibles_expuestos"] == False, "CRÍTICO: La API de reportes está exponiendo datos privados en formato JSON."
