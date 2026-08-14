import os
import pytest

# =====================================================================
# 🤖 SIMULADOR DEL MOTOR DE SEGURIDAD (READING SECRETS)
# =====================================================================


def obtener_llave_gcp_del_sistema() -> str:
    """
    Busca la variable de entorno segura en el sistema operativo.
    Si no existe o está vacía, arroja un error de seguridad.
    """
    # Buscamos la variable en el sistema operativo usando el módulo "os"
    variable_segura = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS_JSON")

    if not variable_segura:
        raise ValueError(
            "CRÍTICO: No se encontró la variable de entorno segura en este sistema.")

    return variable_segura


# =====================================================================
# 🧪 SUITE DE PRUEBAS DE SEGURIDAD DE PIPELINES CON PYTEST
# =====================================================================

# Prueba 1: Verificar el manejo de errores si las variables no están configuradas (Local)
def test_pipeline_seguridad_sin_credenciales_debe_fallar():
    print("\n[Pipeline QA] Verificando que el sistema falle si las variables seguras no existen...")

    # 1. Aseguramos que la variable no esté en nuestra máquina de práctica para esta prueba
    if "GOOGLE_APPLICATION_CREDENTIALS_JSON" in os.environ:
        del os.environ["GOOGLE_APPLICATION_CREDENTIALS_JSON"]

    # 2. Afirmamos que la función debe arrojar un ValueError por falta de seguridad
    with pytest.raises(ValueError) as error_info:
        obtener_llave_gcp_del_sistema()

    assert "CRÍTICO" in str(error_info.value)
    print("✅ El sistema se protegió correctamente. No se puede iniciar sin credenciales.")


# Prueba 2: Simular la inyección del secreto real (Cómo correría en GitHub Actions)
def test_pipeline_inyeccion_secreta_exitosa():
    print("\n[Pipeline QA] Simulando la inyección exitosa de un secreto encriptado en la nube...")

    # 1. Simulamos lo que hace GitHub Actions: inyectar el secreto en la variable de entorno
    llave_encriptada_falsa = '{"type": "service_account", "project_id": "aaa-alliance-prod", "private_key": "XXXXX"}'
    os.environ["GOOGLE_APPLICATION_CREDENTIALS_JSON"] = llave_encriptada_falsa

    # 2. Ejecutamos la función de seguridad
    resultado_secreto = obtener_llave_gcp_del_sistema()

    # 3. Validamos que la variable contenga el valor encriptado correcto de forma confidencial
    assert "service_account" in resultado_secreto
    assert "aaa-alliance-prod" in resultado_secreto

    # Limpiamos la variable al terminar para mantener el entorno seguro
    del os.environ["GOOGLE_APPLICATION_CREDENTIALS_JSON"]
    print("✅ Secreto inyectado y leído de forma 100% exitosa y segura.")
