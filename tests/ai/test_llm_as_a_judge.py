import pytest

# =====================================================================
# ⚖️ SIMULADOR DEL MODELO JUEZ (LLM-AS-A-JUDGE ENGINE)
# =====================================================================


def modelo_juez_evaluar_respuesta(pregunta_usuario: str, respuesta_chatbot: str) -> dict:
    """
    Simula la ejecución de un Modelo de IA Evaluador (Juez).
    Analiza la respuesta del chatbot bajo una rúbrica estricta de Calidad.
    Devuelve un reporte estructurado en formato de diccionario (JSON).
    """
    # RÚBRICA DE EVALUACIÓN:
    # 1. Cortés (Debe saludar o usar un tono amable)
    # 2. Útil (Debe dar una solución o responder a la duda)
    # 3. Conciso (No debe dar rodeos innecesarios)

    puntuacion_final = 5  # Iniciamos con nota perfecta (5 de 5)
    comentarios = []

    resp_lower = respuesta_chatbot.lower()

    # Evaluación de Cortesía
    if not any(saludo in resp_lower for saludo in ["hola", "confirmado", "gusto", "asistente"]):
        puntuacion_final -= 1
        comentarios.append(
            "Falta de cortesía: La respuesta no incluye un saludo o tono amable.")

    # Evaluación de Utilidad
    if "no logré entender" in resp_lower or "repetirla" in resp_lower:
        puntuacion_final -= 2
        comentarios.append(
            "Baja utilidad: El chatbot no logró resolver la duda del usuario.")

    # Evaluación de Concisión (Evitar textos demasiado largos que frustren al usuario)
    if len(respuesta_chatbot.split()) > 30:
        puntuacion_final -= 1
        comentarios.append(
            "Falta de concisión: La respuesta es demasiado larga y puede confundir.")

    # Retornamos el reporte estructurado que leería nuestro test
    return {
        "score_calidad": puntuacion_final,
        "comentarios_juez": comentarios,
        "aprobado": puntuacion_final >= 4  # Aprobamos solo si la nota es 4 o 5
    }

# =====================================================================
# 🧪 QUALITY GATE SUITE - LLM-AS-A-JUDGE
# =====================================================================


def test_juez_aprueba_respuesta_excelente():
    """Valida que el modelo juez apruebe una respuesta que cumple con toda la rúbrica."""
    print("\n\n[LLM-as-a-Judge] Evaluando respuesta de alta calidad...")

    pregunta = "Hola, ¿me pueden ayudar con una grúa?"
    # Respuesta cortés, útil y concisa
    respuesta_bot = "🤖 Hola! Con mucho gusto. Confirmado, tu membresía incluye el servicio de grúa de forma gratuita."

    # El Juez hace la auditoría
    reporte_evaluacion = modelo_juez_evaluar_respuesta(pregunta, respuesta_bot)

    print(f"📊 Reporte del Juez de IA:")
    print(f"  - Nota de Calidad: {reporte_evaluacion['score_calidad']}/5")
    print(
        f"  - Comentarios de mejora: {reporte_evaluacion['comentarios_juez']}")
    print(f"  - ¿Aprobado para producción?: {reporte_evaluacion['aprobado']}")

    # El Quality Gate exige que el reporte del Juez esté aprobado (Aprobado = True)
    assert reporte_evaluacion["aprobado"] is True, (
        f"FAIL: El Juez de IA rechazó la respuesta con nota: {reporte_evaluacion['score_calidad']}/5"
    )
    print("🏆 QUALITY GATE: APROBADO POR EL JUEZ DE IA")


def test_juez_rechaza_respuesta_deficiente_debe_fallar():
    """Valida que el modelo juez detecte y repruebe una respuesta que no ayuda al usuario."""
    print("\n\n[LLM-as-a-Judge] Evaluando respuesta deficiente...")

    pregunta = "Necesito cambiar mi tarjeta de pago"
    # El chatbot falla en entender y da una respuesta robótica y fría
    respuesta_bot = "No logré entender tu solicitud, ¿podrías repetirla?"

    reporte_evaluacion = modelo_juez_evaluar_respuesta(pregunta, respuesta_bot)

    print(f"📊 Reporte del Juez de IA:")
    print(f"  - Nota de Calidad: {reporte_evaluacion['score_calidad']}/5")
    print(
        f"  - Comentarios de mejora: {reporte_evaluacion['comentarios_juez']}")
    print(f"  - ¿Aprobado para producción?: {reporte_evaluacion['aprobado']}")

    # Esperamos que el Juez de IA repruebe este comportamiento y el assert lance AssertionError
    with pytest.raises(AssertionError):
        assert reporte_evaluacion["aprobado"] is True, "FAIL: El Juez de IA no debió aprobar esta respuesta."

    print("✅ Quality Gate Exitoso: El Juez de IA detectó y bloqueó la respuesta deficiente.")
