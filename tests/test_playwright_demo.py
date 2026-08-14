import pytest
from playwright.sync_api import sync_playwright
from pages.PlaywrightDemoPage import PlaywrightDemoPage


def test_busqueda_playwright_con_pom():
    print("\n🚀 Iniciando prueba de automatización con arquitectura POM (Playwright)...")

    with sync_playwright() as p:
        # Lanzamos el navegador visible para ver el flujo real
        navegador = p.chromium.launch(headless=False, slow_mo=500)
        pagina = navegador.new_page()

        # 1. Inicializamos nuestra página usando el molde POM
        demo_page = PlaywrightDemoPage(pagina)

        # 2. Ejecutamos las acciones de forma ultra-limpia
        demo_page.navegar_a_wikipedia()
        demo_page.buscar_tema("Inteligencia Artificial")

        # 3. Hacemos la validación de QA (Aserción de UI)
        titulo_real = demo_page.obtener_titulo_articulo()
        print(
            f"🎯 Validando que el título del artículo sea correcto. Título real: '{titulo_real}'")

        assert titulo_real == "Inteligencia artificial", f"Error: Se esperaba 'Inteligencia artificial' pero se obtuvo '{titulo_real}'"

        # 4. Tomamos evidencia y cerramos
        pagina.screenshot(path="evidencia_playwright_pom.png")
        navegador.close()
        print("✅ Prueba completada exitosamente con arquitectura profesional POM.")
