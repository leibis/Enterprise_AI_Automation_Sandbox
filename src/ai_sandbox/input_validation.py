# =====================================================================
# 🌪️ CHAOS TESTING - INPUT RESILIENCE FOR AI APPLICATIONS
# =====================================================================

MAX_CARACTERES_MENSAJE = 500


def procesar_mensaje_con_limite(mensaje_usuario: str) -> str:
    """
    Simula la capa de entrada de un chatbot.

    Antes de enviar un mensaje a un LLM, valida:
    - que el dato sea texto;
    - que no supere el límite permitido.

    El objetivo es evitar costos, latencia y errores por entradas excesivas.
    """

    # Validación de tipo: el chatbot espera texto, no números ni listas.
    if not isinstance(mensaje_usuario, str):
        raise TypeError(
            "Entrada inválida: el mensaje del usuario debe ser un texto."
        )

    # Validación de longitud: evita enviar mensajes excesivos al LLM.
    if len(mensaje_usuario) > MAX_CARACTERES_MENSAJE:
        return (
            "⚠️ Tu mensaje es demasiado largo. "
            "Por favor, resume tu solicitud e inténtalo nuevamente."
        )

    # Simulación de una respuesta normal del chatbot.
    return "🤖 Mensaje recibido correctamente. ¿Cómo puedo ayudarte?"
