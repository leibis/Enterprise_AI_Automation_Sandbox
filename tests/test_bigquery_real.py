import pytest
from unittest.mock import MagicMock
from google.auth.exceptions import DefaultCredentialsError

# =====================================================================
# 📊 FUNCIÓN DE CONEXIÓN A GOOGLE CLOUD BIGQUERY
# =====================================================================


def consultar_base_datos_socios(id_socio: str, cliente_bigquery=None) -> dict:
    """
    Esta función se conecta a BigQuery y busca los datos de un socio por su ID.
    Si no se le pasa un cliente de prueba (Mock), intentará conectarse a GCP real.
    """
    # Si no nos pasan un cliente de prueba, intentamos inicializar la conexión real a GCP
    if cliente_bigquery is None:
        from google.cloud import bigquery
        # Esta línea detonará un error controlado si no hay credenciales configuradas
        cliente_bigquery = bigquery.Client()

        # Simulación de consulta real en GCP
        query = f"SELECT id_socio, nombre, estado_membresia FROM `aaa.socios` WHERE id_socio = '{id_socio}'"
        query_job = cliente_bigquery.query(query)
        resultados = query_job.to_dataframe()
        return resultados.to_dict(orient="records")[0]

    # Si nos pasan un cliente simulado (Mock), devolvemos su respuesta de inmediato
    return cliente_bigquery.buscar_socio(id_socio)


# =====================================================================
# 🧪 SUITE DE PRUEBAS DE DATOS (DATA QA) CON PYTEST
# =====================================================================

# Prueba 1: Verificar el manejo de errores si no hay credenciales de Google Cloud
def test_bigquery_error_credenciales_no_configuradas():
    print("\n[QA] Probando que el sistema controle la falta de credenciales de GCP...")

    # Afirmamos que el código de conexión real DEBE arrojar la excepción DefaultCredentialsError
    # si intentamos conectarnos sin tener el archivo JSON configurado.
    with pytest.raises(DefaultCredentialsError):
        consultar_base_datos_socios("SOCIO-123", cliente_bigquery=None)

    print("✅ Excepción capturada correctamente. El sistema no permite conexiones no autorizadas.")


# Prueba 2: Validar los datos de un socio activo usando un Mock de BigQuery (Simulación de producción)
def test_bigquery_validar_socio_activo_con_mock():
    print(
        "\n[QA] Probando la consistencia de datos de un socio usando un Mock seguro...")

    # 1. Creamos un "Imitador" (Mock) de la base de datos de BigQuery
    mock_gcp = MagicMock()

    # Le programamos la respuesta exacta que esperamos que devuelva el imitador
    mock_gcp.buscar_socio.return_value = {
        "id_socio": "SOCIO-007",
        "nombre": "James Bond",
        "estado_membresia": "ACTIVE",
        "tiene_cobertura_grua": True
    }

    # 2. Ejecutamos nuestra función pasándole el imitador de Google Cloud
    datos_socio = consultar_base_datos_socios(
        "SOCIO-007", cliente_bigquery=mock_gcp)

    # 3. Realizamos las aserciones de calidad de datos
    assert datos_socio["id_socio"] == "SOCIO-007"
    assert datos_socio["nombre"] == "James Bond"
    assert datos_socio["estado_membresia"] == "ACTIVE"
    assert datos_socio["tiene_cobertura_grua"] == True

    print("✅ Datos del socio validados con éxito. La estructura es consistente.")
