# 1. Esta es la función de negocio del chatbot que queremos probar
def verificar_elegibilidad_grua(membresia_estado, tiene_cobertura):
    # Solo es elegible si la membresía está ACTIVE y además tiene la cobertura contratada
    if membresia_estado == "ACTIVE" and tiene_cobertura == True:
        return True
    else:
        return False


# --- CASOS DE PRUEBA DE AUTOMATIZACIÓN CON PYTEST ---


# Caso 1: Socio activo y que SÍ tiene cobertura de grúa contratada (Elegible)
def test_socio_activo_con_cobertura():
    resultado = verificar_elegibilidad_grua(
        membresia_estado="ACTIVE", tiene_cobertura=True
    )
    assert (
        resultado == True
    ), "Error: Un socio activo con cobertura debería ser elegible para la grúa."


# Caso 2: Socio inactivo que tiene marcado cobertura (No elegible)
def test_socio_inactivo_con_cobertura():
    resultado = verificar_elegibilidad_grua(
        membresia_estado="INACTIVE", tiene_cobertura=True
    )
    assert (
        resultado == False
    ), "Error: Un socio inactivo NO debería poder pedir una grúa aunque tenga cobertura marcada."


# Caso 3: Socio activo pero que NO tiene contratada la cobertura (No elegible)
def test_socio_activo_sin_cobertura():
    resultado = verificar_elegibilidad_grua(
        membresia_estado="ACTIVE", tiene_cobertura=False
    )
    assert (
        resultado == False
    ), "Error: Un socio activo pero sin la cobertura contratada no debería ser elegible."
