import pytest
from pydantic import BaseModel, Field, ValidationError
pytestmark = pytest.mark.ai
# =====================================================================
# 📋 DEFINICIÓN DEL FORMULARIO ESTRICTO (Pydantic Model)
# =====================================================================


class ReporteEvaluacionJuez(BaseModel):
    """
    Define la estructura exacta y obligatoria que debe tener 
    el reporte de calidad de nuestro Juez de IA.
    """
    # El campo score_calidad debe ser un número entero entre 1 y 5
    score_calidad: int = Field(..., ge=1, le=5,
                               description="Calificación de 1 a 5")

    # El campo aprobado debe ser un valor booleano (True o False)
    aprobado: bool = Field(...,
                           description="Determina si la respuesta pasa el Quality Gate")

    # El campo comentarios_juez debe ser una lista de textos (strings)
    comentarios_juez: list[str] = Field(
        default=[], description="Lista de sugerencias de mejora")

# =====================================================================
# 🧠 SIMULADOR DE JUEZ DE IA USANDO PYDANTIC (LLM-as-a-Judge)
# =====================================================================


def generar_reporte_juez_ia_pydantic(score: int, aprobado: bool, comentarios: list) -> ReporteEvaluacionJuez:
    """
    Simula el output del LLM Juez y lo valida a través de nuestro modelo de Pydantic.
    Si los tipos de datos son incorrectos, Pydantic lanzará un ValidationError automáticamente.
    """
    # Creamos e instanciamos el modelo de Pydantic
    return ReporteEvaluacionJuez(
        score_calidad=score,
        aprobado=aprobado,
        comentarios_juez=comentarios
    )

# =====================================================================
# 🧪 SUITE DE PRUEBAS DE ESTRUCTURAS DE DATOS (Quality Gates)
# =====================================================================


def test_pydantic_valida_reporte_correcto_exitosamente():
    """Valida que un reporte con estructura perfecta pase la validación de Pydantic sin problemas."""
    print("\n\n[Pydantic QA] Validando reporte correcto...")

    # Simulamos un reporte perfecto (score es entero, aprobado es boolean, comentarios es lista)
    reporte = generar_reporte_juez_ia_pydantic(
        score=5,
        aprobado=True,
        comentarios=["Respuesta muy cortés y concisa."]
    )

    # Verificamos que Pydantic haya creado el objeto correctamente
    assert reporte.score_calidad == 5
    assert reporte.aprobado is True
    print(
        f"✅ Reporte validado con éxito. Score: {reporte.score_calidad}, Aprobado: {reporte.aprobado}")


def test_pydantic_detecta_y_bloquea_datos_invalidos_debe_fallar():
    """Valida que Pydantic detecte si el LLM intentó enviar un dato inválido (ej. un score fuera de rango)."""
    print("\n\n[Pydantic QA] Validando detección de datos corruptos...")

    # El LLM Juez cometió un error e intentó enviar un score de "10" (El límite máximo permitido es 5)
    with pytest.raises(ValidationError) as error_info:
        generar_reporte_juez_ia_pydantic(
            score=10,  # ❌ Dato inválido fuera de rango
            aprobado=True,
            comentarios=[]
        )

    # Verificamos que Pydantic haya bloqueado el registro y lanzado el ValidationError esperado
    print("✅ Pydantic bloqueó con éxito la estructura de datos corrupta.")
    print(
        f"🚨 Detalle del error de validación de Pydantic:\n{error_info.value}")
