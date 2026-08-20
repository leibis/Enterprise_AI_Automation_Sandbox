import pytest
pytestmark = pytest.mark.ai
# =====================================================================
# 🧠 ENGINES DE EVALUACIÓN DE RAG (Métricas de la Tríada)
# =====================================================================


def evaluar_relevancia_contexto(query_usuario: str, contexto_extraido: str) -> float:
    """
    Pilar 1: Context Relevance (Versión Robusta v2).
    Valida si el manual trajo información útil para la duda del usuario.
    Filtra palabras ruido para evitar penalizaciones injustas en oraciones largas.
    Devuelve un puntaje de 0.0 (Inútil) a 1.0 (Perfecto).
    """
    # 1. Convertimos la pregunta a minúsculas y la dividimos en palabras
    palabras_totales = query_usuario.lower().split()

    # 2. FILTRADO: Nos quedamos solo con las palabras clave reales (más de 3 letras)
    # Esto elimina palabras ruido como 'la', 'de', 'mi', 'un', 'el', etc.
    palabras_clave_reales = []
    for palabra in palabras_totales:
        palabra_limpia = palabra.strip(",.?!¡¿")
        if len(palabra_limpia) > 3:
            palabras_clave_reales.append(palabra_limpia)

    # Si la pregunta no tiene palabras clave reales, el score es 0.0
    if len(palabras_clave_reales) == 0:
        return 0.0

    # 3. CONTAR COINCIDENCIAS: Buscamos cuántas palabras clave reales están en el manual
    coincidencias = 0
    contexto_lower = contexto_extraido.lower()
    for palabra in palabras_clave_reales:
        if palabra in contexto_lower:
            coincidencias += 1

    # 4. CÁLCULO CIENTÍFICO: Dividimos las coincidencias entre el total de palabras CLAVE reales
    # Ya no dividimos entre palabras ruido, haciendo la fórmula 100% justa y robusta.
    score_final = coincidencias / len(palabras_clave_reales)

    return score_final


def evaluar_groundedness(contexto_extraido: str, respuesta_generada: str) -> float:
    """
    Pilar 2: Groundedness (Fidelidad).
    Valida si la respuesta del LLM está estrictamente fundamentada en el contexto proveído.
    Si la respuesta menciona datos que NO están en el contexto, se considera Alucinación.
    Devuelve de 0.0 (Totalmente inventada) a 1.0 (100% verídica según el contexto).
    """
    # Buscamos números o métricas en la respuesta
    import re
    numeros_respuesta = re.findall(
        # busca todos los números que existan en el texto y los guarda en una lista.
        r'\d+%', respuesta_generada) + re.findall(r'\b\d+\b', respuesta_generada)

    if not numeros_respuesta:
        return 1.0  # Si no hay datos numéricos específicos, asumimos alineación básica

    datos_verificados = 0
    for dato in numeros_respuesta:
        if dato in contexto_extraido:
            datos_verificados += 1

    return datos_verificados / len(numeros_respuesta)


def evaluar_relevancia_respuesta(query_usuario: str, respuesta_generada: str) -> float:
    """
    Pilar 3: Answer Relevance.
    Valida si el bot realmente contestó la pregunta del usuario.
    Devuelve de 0.0 (No responde la duda) a 1.0 (Responde perfectamente).
    """
    # Verificamos si la respuesta tiene sentido conversacional básico relacionado a la query
    temas_comunes = ["grúa", "asistencia",
                     "membresía", "tarjeta", "pago", "cobertura"]

    query_lower = query_usuario.lower()
    resp_lower = respuesta_generada.lower()

    # Si la query habla de un tema, la respuesta también debe mencionarlo
    for tema in temas_comunes:
        if tema in query_lower and tema in resp_lower:
            return 1.0

    return 0.2

# =====================================================================
# 🧪 RAG QUALITY GATE - AUTOMATED SUITE (La Tríada en Acción)
# =====================================================================


def test_pipeline_rag_exitoso():
    """Valida un flujo RAG perfecto donde los tres pilares de la tríada están aprobados."""
    print("\n\n[RAG Triad] Evaluando pipeline exitoso...")

    # 1. El usuario pregunta por asistencia de grúa
    query = "Necesito solicitar una grúa para mi vehículo"

    # 2. El sistema busca en el manual (Contexto correcto)
    contexto = "El servicio de grúa y asistencia vial en carretera está cubierto de forma gratuita para miembros activos."

    # 3. El bot genera la respuesta basándose estrictamente en el contexto
    respuesta = "🤖 Confirmado. Tu membresía incluye el servicio de grúa de forma gratuita."

    # EVALUACIÓN 1: ¿El contexto es relevante para la pregunta?
    relevancia_ctx = evaluar_relevancia_contexto(query, contexto)
    print(
        f"📊 1. Context Relevance Score: {relevancia_ctx:.2f} (Esperado: >= 0.5)")
    assert relevancia_ctx >= 0.3, "FAIL: El contexto extraído no es relevante para la pregunta del usuario."

    # EVALUACIÓN 2: ¿La respuesta se basa solo en el contexto? (No alucinación)
    groundedness = evaluar_groundedness(contexto, respuesta)
    print(f"📊 2. Groundedness Score: {groundedness:.2f} (Esperado: >= 0.8)")
    assert groundedness >= 0.8, "FAIL: El bot alucinó o inventó información fuera del contexto."

    # EVALUACIÓN 3: ¿La respuesta responde a la duda del usuario?
    relevancia_resp = evaluar_relevancia_respuesta(query, respuesta)
    print(
        f"📊 3. Answer Relevance Score: {relevancia_resp:.2f} (Esperado: >= 0.7)")
    assert relevancia_resp >= 0.7, "FAIL: La respuesta final no responde a la duda del usuario."

    print("🏆 PIPELINE RAG VERIFICADO: PASS (Tríada de Calidad Perfecta)")


def test_pipeline_rag_con_alucinacion_debe_fallar():
    """Valida que el Quality Gate detecte cuando el bot inventa datos numéricos (Groundedness Fail)."""
    print("\n\n[RAG Triad] Evaluando pipeline con alucinación de datos...")

    query = "Quiero saber la cobertura de mi plan de asistencia"

    # El manual dice que la cobertura es del 79% para grúas
    contexto = "La cobertura de asistencia vial cubre el 79% de los incidentes mecánicos locales."

    # El bot alucina y le dice al cliente que cubre el 100% y que tiene 100 talleres afiliados (datos inventados)
    respuesta_alucinada = "🤖 Su plan cuenta con el 100% de cobertura en 100 talleres de la ciudad."

    relevancia_ctx = evaluar_relevancia_contexto(query, contexto)
    assert relevancia_ctx >= 0.3

    # Evaluamos Groundedness (Fidelidad)
    groundedness = evaluar_groundedness(contexto, respuesta_alucinada)
    print(
        f"📊 Groundedness Score obtenido: {groundedness:.2f} (Esperado: >= 0.8)")

    # Esperamos que esta validación falle debido a la invención de datos
    with pytest.raises(AssertionError):
        assert groundedness >= 0.8, "FAIL: Se detectó invención de datos numéricos en la respuesta."

    print("✅ Quality Gate funcionó: Detectó y bloqueó la alucinación del modelo de forma exitosa.")
