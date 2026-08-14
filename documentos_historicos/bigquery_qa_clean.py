import os
from google.auth.exceptions import DefaultCredentialsError
from google.cloud import bigquery


def ejecutar_auditoria_datos():
       print("--- INICIANDO AUDITORÍA DE DATOS DE SOCIOS (AAA) ---")

       # 1. Intentamos inicializar el cliente de BigQuery
       try:
            cliente = bigquery.Client()
            print("✅ Conectado exitosamente a Google Cloud BigQuery.")

            consulta_anomalia = """
            SELECT id_socio, nombre, estado_membresia, tiene_cobertura_grua
            FROM `aaa-club-alliance.data_warehouse.socios`
            WHERE estado_membresia = 'INACTIVE' AND tiene_cobertura_grua = TRUE
        """

            print("[QA] Ejecutando consulta de auditoría de anomalías...")
            query_job = cliente.query(consulta_anomalia)
            resultados = query_job.to_dataframe()

            total_anomalias = len(resultados)

            if total_anomalias == 0:
                print(
                    "✅ TEST PASADO: No se encontraron anomalías. Los socios inactivos no tienen beneficios activos."
                )
            else:
                print(
                    f"❌ TEST FALLIDO: Se encontraron {total_anomalias} socios inactivos con cobertura activa."
                )
                print(resultados)
       
       except DefaultCredentialsError:
            print("\n⚠️ ERROR DE AUTENTICACIÓN CONTROLADO (Esperado para hoy):")
            print("No se encontraron credenciales de Google Cloud (archivo JSON).")
            print(
                "Para solucionar esto en el trabajo real, debemos configurar la variable de entorno:"
            )
            print('set GOOGLE_APPLICATION_CREDENTIALS="ruta/a/tu/llave.json"')

            print(
                "\n💡 Simulando cómo procesaríamos el resultado de BigQuery si las credenciales existieran:"
            )
            anomalias_simuladas = [
                {
                    "id_socio": "SOCIO-007",
                    "nombre": "James Bond",
                    "estado_membresia": "INACTIVE",
                    "tiene_cobertura_grua": True,
                }
            ]

            print(
                f"❌ TEST FALLIDO (Simulado): Se encontró {len(anomalias_simuladas)} anomalía en la base de datos."
            )
            print(
                f"Socio con error: {anomalias_simuladas[0]['nombre']} ({anomalias_simuladas[0]['id_socio']}) tiene cobertura de grúa pero su membresía está INACTIVA."
            )


ejecutar_auditoria_datos()
