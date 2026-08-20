import pytest
pytestmark = pytest.mark.api
# =====================================================================
# 🤖 SIMULADOR DEL MOTOR DE APIs DE LA AAA (MÉTODOS POST/PUT/DELETE)
# =====================================================================

# Esta base de datos simulada en memoria nos servirá para las pruebas
BASE_DATOS_REPORTES = {
    "REP-101": {"id": "REP-101", "region": "NORTHEAST", "estado": "PENDIENTE"}
}


def simular_api_aaa(metodo: str, endpoint: str, datos=None) -> dict:
    """
    Simula el comportamiento de una API real para crear, actualizar y borrar reportes.
    """
    metodo_clean = metodo.upper()

    # ─── 1. MÉTODO POST (Crear un nuevo reporte) ───
    if metodo_clean == "POST" and endpoint == "/v1/reports":
        if not datos or "id" not in datos or "region" not in datos:
            return {"status_code": 400, "error": "Datos incompletos para crear el reporte."}

        nuevo_id = datos["id"]
        BASE_DATOS_REPORTES[nuevo_id] = {
            "id": nuevo_id,
            "region": datos["region"],
            "estado": "CREADO"
        }
        return {
            "status_code": 201,  # 201 significa "Created" (Creado con éxito)
            "mensaje": f"Reporte {nuevo_id} creado exitosamente.",
            "datos": BASE_DATOS_REPORTES[nuevo_id]
        }

    # ─── 2. MÉTODO PUT (Actualizar un reporte existente) ───
    elif metodo_clean == "PUT" and "/v1/reports/" in endpoint:
        # Extraemos el ID del endpoint (ejemplo: "/v1/reports/REP-101" -> "REP-101")
        reporte_id = endpoint.split("/")[-1]

        if reporte_id not in BASE_DATOS_REPORTES:
            return {"status_code": 404, "error": f"El reporte {reporte_id} no existe."}

        if not datos or "estado" not in datos:
            return {"status_code": 400, "error": "Falta el campo 'estado' para actualizar."}

        # Actualizamos el estado en nuestra base de datos simulada
        BASE_DATOS_REPORTES[reporte_id]["estado"] = datos["estado"]
        return {
            "status_code": 200,  # 200 significa "OK" (Éxito)
            "mensaje": f"Reporte {reporte_id} actualizado exitosamente.",
            "datos": BASE_DATOS_REPORTES[reporte_id]
        }

    # ─── 3. MÉTODO DELETE (Borrar un reporte) ───
    elif metodo_clean == "DELETE" and "/v1/reports/" in endpoint:
        reporte_id = endpoint.split("/")[-1]

        if reporte_id not in BASE_DATOS_REPORTES:
            return {"status_code": 404, "error": f"No se pudo borrar. El reporte {reporte_id} no existe."}

        # Eliminamos el registro de la base de datos
        del BASE_DATOS_REPORTES[reporte_id]
        return {
            "status_code": 200,
            "mensaje": f"Reporte {reporte_id} eliminado de la base de datos de forma segura."
        }

    return {"status_code": 405, "error": "Método no permitido."}


# =====================================================================
# 🧪 SUITE DE PRUEBAS DE API AVANZADA CON PYTEST
# =====================================================================

# Prueba 1: Crear un reporte con POST (Camino Feliz)
def test_post_crear_reporte_exitoso():
    print("\n[API QA] Probando la creación de un nuevo reporte usando POST...")
    datos_envio = {"id": "REP-202", "region": "MIDWEST"}

    # Ejecutamos la petición POST
    respuesta = simular_api_aaa("POST", "/v1/reports", datos=datos_envio)

    # Validamos que la API responda con el código de creación correcto (201)
    assert respuesta["status_code"] == 201
    assert "creado exitosamente" in respuesta["mensaje"]
    assert respuesta["datos"]["region"] == "MIDWEST"
    assert respuesta["datos"]["estado"] == "CREADO"


# Prueba 2: Actualizar el estado de un reporte existente con PUT
def test_put_actualizar_reporte_exitoso():
    print("\n[API QA] Probando la actualización de un reporte existente usando PUT...")
    datos_actualizacion = {"estado": "APROBADO"}

    # Actualizamos el reporte "REP-101" que ya existe en nuestra base de datos
    respuesta = simular_api_aaa(
        "PUT", "/v1/reports/REP-101", datos=datos_actualizacion)

    # Validamos el éxito de la actualización (200 OK)
    assert respuesta["status_code"] == 200
    assert respuesta["datos"]["estado"] == "APROBADO"


# Prueba 3: Borrar un reporte de forma segura con DELETE
def test_delete_borrar_reporte_exitoso():
    print("\n[API QA] Probando la eliminación segura de un reporte usando DELETE...")

    # Intentamos borrar el reporte "REP-202" que creamos en la Prueba 1
    respuesta = simular_api_aaa("DELETE", "/v1/reports/REP-202")

    # Validamos que el borrado haya sido exitoso
    assert respuesta["status_code"] == 200
    assert "eliminado" in respuesta["mensaje"]
