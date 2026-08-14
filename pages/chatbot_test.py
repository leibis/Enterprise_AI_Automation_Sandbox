import time
from unittest.mock import MagicMock

# 1. Esta función simula la consulta real a GCP BigQuery
def consultar_bigquery_real(id_socio):
    print(f"[BigQuery] Conectando a Google Cloud para el socio {id_socio}...")
    time.sleep(5)  # Simula que la red está lenta (tarda 5 segundos)
    return {"id": id_socio, "tiene_cobertura_grua": True}

# 2. Esta es la lógica de nuestro Chatbot de AAA
def chatbot_responder(id_socio, consulta_db_funcion):
    print("\n🤖 Chatbot: ¡Hola! Permíteme verificar tus datos de socio...")
    
    # Llamamos a la función de base de datos que nos pasen
    datos_socio = consulta_db_funcion(id_socio)
    
    if datos_socio["tiene_cobertura_grua"]:
        return "🤖 Chatbot: ¡Confirmado! Tu membresía activa incluye servicio de grúa gratis. Te enviaremos ayuda de inmediato."
    else:
        return "🤖 Chatbot: Lo siento, tu membresía actual no incluye grúa. ¿Deseas adquirirla ahora?"

# --- CASO DE PRUEBA DE QA ---
print("--- PRUEBA 1: USANDO LA CONEXIÓN REAL (Lenta y dependiente) ---")
inicio = time.time()
respuesta_real = chatbot_responder("SOCIO-999", consultar_bigquery_real)
print(respuesta_real)
print(f"⏱️ Tiempo total de la prueba: {time.time() - inicio:.2f} segundos")

print("\n--------------------------------------------------------------")

print("--- PRUEBA 2: USANDO MOCKING (Ultra rápida y 100% aislada) ---")
inicio = time.time()

# Creamos un "Socio Falso" (Mock) que responde de inmediato sin ir a Google Cloud
consultar_bigquery_mock = MagicMock()
consultar_bigquery_mock.return_value = {"id": "SOCIO-999", "tiene_cobertura_grua": True}

# Ejecutamos el chatbot usando nuestro Mock en lugar de la función real
respuesta_mock = chatbot_responder("SOCIO-999", consultar_bigquery_mock)
print(respuesta_mock)
print(f"⏱️ Tiempo total de la prueba: {time.time() - inicio:.2f} segundos")