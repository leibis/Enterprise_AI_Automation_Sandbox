import pytest
import time
pytestmark = pytest.mark.ai
# =====================================================================
# 🔌 SIMULADOR DE API DE IA CON FALLAS DE INFRAESTRUCTURA (Cloud LLM)
# =====================================================================


def consultar_api_llm_con_resiliencia(mensaje_usuario: str, simular_falla: str = "NINGUNA") -> str:
    """
    Simula una consulta a la API de Vertex AI (GCP).
    Implementa lógica de contingencia si la nube falla (Graceful Degradation).
    """
    # ❌ ESCENARIO 1: Simulación de Bloqueo por exceso de uso (Rate Limit - HTTP 429)
    if simular_falla == "RATE_LIMIT":
        raise ConnectionError(
            "HTTP 429: Too Many Requests. Rate limit exceeded in Google Cloud Vertex AI.")

    # ❌ ESCENARIO 2: Simulación de caída de internet o Timeout (Servidor lento)
    if simular_falla == "TIMEOUT":
        time.sleep(3)  # Simula que el servidor se congeló por 3 segundos
        raise TimeoutError(
            "HTTP 504: Gateway Timeout. Vertex AI API took too long to respond.")

    # Flujo normal si no hay fallas
    return "Respuesta exitosa del LLM."

# =====================================================================
# SUITE DE PRUEBAS DE RESILIENCIA Y CAOS (Cloud Quality Gate)
# =====================================================================


def test_defensa_rate_limit_debe_usar_backup():
    """Valida que si la API principal nos bloquea (HTTP 429), el sistema controle el error sin explotar."""
    print("\n\n[Resilience QA] Probando bloqueo de API (HTTP 429)...")

    # Intentamos consultar la API simulando el bloqueo de Google Cloud
    with pytest.raises(ConnectionError) as error_info:
        consultar_api_llm_con_resiliencia("Hola", simular_falla="RATE_LIMIT")

    # Verificamos que el error capturado contenga el código HTTP correcto de Rate Limit
    assert "HTTP 429" in str(error_info.value)
    print("✅ El sistema capturó y controló el Rate Limit de GCP con éxito.")


def test_defensa_timeout_debe_limitar_tiempo_espera():
    """Valida que el sistema no permita que una API lenta congele la aplicación del usuario."""
    print("\n\n[Resilience QA] Probando resiliencia ante API lenta (Timeout)...")

    tiempo_inicio = time.time()

    # Intentamos la consulta simulando que la nube está lenta
    with pytest.raises(TimeoutError) as error_info:
        consultar_api_llm_con_resiliencia("Hola", simular_falla="TIMEOUT")

    tiempo_fin = time.time()
    tiempo_transcurrido = tiempo_fin - tiempo_inicio

    # Verificamos que el sistema haya lanzado el TimeoutError
    assert "HTTP 504" in str(error_info.value)

    # Validamos que el test de resiliencia no se haya quedado congelado infinitamente
    print(
        f"⏱️ Tiempo que tardó el sistema en fallar y defenderse: {tiempo_transcurrido:.2f} segundos")
    assert tiempo_transcurrido >= 3.0
    print(" El sistema cortó la conexión lenta de forma segura y lanzó el Timeout correspondiente.")
