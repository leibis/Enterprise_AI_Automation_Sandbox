# Una función de negocio que calcula el costo del remolque
# Los socios de la AAA tienen un descuento del 10%
def calcular_costo_remolque(distancia_km, es_socio):
    costo_por_km = 5.0
    total = distancia_km * costo_por_km

    if es_socio:
        total = total * 0.90

    return total

# --- NUESTRAS PRUEBAS DE AUTOMATIZACIÓN ---


# Prueba 1: Verificar el costo para un Socio

def test_costo_remolque_para_socio():
    resultado = calcular_costo_remolque(distancia_km=10, es_socio=True)
    # Afirmamos que el costo para un socio por 10km debe ser exactamente $45.0
    assert resultado == 45.0

# Prueba 2: Verificar el costo para un No Socio


def test_costo_remolque_para_no_socio():
    resultado = calcular_costo_remolque(distancia_km=10, es_socio=False)
    # Afirmamos que para alguien que no es socio debe costar exactamente $50.0
    assert resultado == 50.0
