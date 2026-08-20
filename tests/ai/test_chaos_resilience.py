import pytest
from src.ai_sandbox.input_validation import procesar_mensaje_con_limite
pytestmark = pytest.mark.ai

# =====================================================================
# 🧪 CHAOS TEST SUITE - CONTROLLED FAILURE SCENARIOS
# =====================================================================


def test_chatbot_acepta_mensaje_normal():
    """Valida que un mensaje dentro del límite sea procesado normalmente."""

    print("\n[Chaos QA] Validando mensaje de tamaño normal...")

    mensaje = "Necesito ayuda con mi membresía."
    respuesta = procesar_mensaje_con_limite(mensaje)

    assert "Mensaje recibido correctamente" in respuesta
    print("✅ El chatbot procesó un mensaje normal correctamente.")


def test_chatbot_rechaza_mensaje_demasiado_largo():
    """
    Valida que una entrada excesiva no llegue al LLM.
    El sistema debe responder de forma segura y controlada.
    """

    print("\n[Chaos QA] Enviando mensaje excesivamente largo...")

    # Creamos un texto de 501 caracteres: supera el límite de 500.
    mensaje_excesivo = "A" * 501

    respuesta = procesar_mensaje_con_limite(mensaje_excesivo)

    assert "demasiado largo" in respuesta
    assert "resume tu solicitud" in respuesta
    print("✅ El sistema rechazó la entrada excesiva sin colapsar.")


def test_chatbot_rechaza_tipo_de_dato_invalido():
    """
    Valida que el sistema rechace tipos de datos incorrectos.
    Un chatbot debe recibir texto, no estructuras inesperadas.
    """

    print("\n[Chaos QA] Enviando tipo de dato inválido...")

    mensaje_invalido = ["Necesito ayuda", "Esto no es un texto único"]

    with pytest.raises(TypeError) as error_info:
        procesar_mensaje_con_limite(mensaje_invalido)

    assert "debe ser un texto" in str(error_info.value)
    print("✅ El sistema bloqueó correctamente el tipo de dato inválido.")
