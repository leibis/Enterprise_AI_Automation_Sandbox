import time
from playwright.sync_api import sync_playwright


def correr_mi_primer_test_visual():
    print("🚀 Iniciando el motor de Playwright...")

    # 1. Iniciamos Playwright de forma síncrona
    with sync_playwright() as p:
        print("🌐 Abriendo navegador Chromium en modo visible (Headed)...")

        # 2. Lanzamos el navegador Chromium
        # headless=False: Hace que podamos ver físicamente la ventana del navegador abierta
        # slow_mo=1000: Agrega una pausa de 1 segundo (1000 ms) entre cada acción para que tus ojos puedan seguir el flujo
        navegador = p.chromium.launch(headless=False, slow_mo=1000)

        # 3. Abrimos una nueva pestaña o página en el navegador
        pagina = navegador.new_page()

        print("🌍 Navegando a la página de inicio de Wikipedia...")
        # 4. Viajamos a una URL real de internet
        pagina.goto("https://es.wikipedia.org/")

        print("🔍 Buscando el cuadro de búsqueda en la pantalla...")
        # 5. Buscamos el cuadro de búsqueda de Wikipedia por su atributo de marcador (placeholder)
        cuadro_busqueda = pagina.get_by_placeholder(
            "Buscar en Wikipedia").first

        print("✏️ Escribiendo 'Inteligencia Artificial' en el cuadro...")
        # 6. Escribimos nuestro texto de búsqueda
        cuadro_busqueda.fill("Inteligencia Artificial")

        print("⌨️ Presionando la tecla Enter para buscar...")
        # 7. Presionamos la tecla "Enter" en nuestro teclado simulado
        cuadro_busqueda.press("Enter")

        # Le damos 2 segundos para que termine de cargar la página de resultados
        time.sleep(2)

        print("📸 Tomando una captura de pantalla de evidencia...")
        # 8. Tomamos una captura de pantalla de la página de resultados y la guardamos en tu carpeta
        pagina.screenshot(path="resultado_wikipedia.png")

        print("🔒 Cerrando el navegador de forma limpia...")
        # 9. Cerramos la sesión del navegador para liberar memoria de tu computadora
        navegador.close()

        print("\n✅ TEST COMPLETADO EXITOSAMENTE. ¡Mira tu carpeta de archivos!")


# Ejecutamos la función de prueba
correr_mi_primer_test_visual()
