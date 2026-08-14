from playwright.sync_api import Page


class PlaywrightDemoPage:
    def __init__(self, page: Page):
        self.page = page
        # Nuestro localizador seguro con el .first para evitar la violación de modo estricto
        self.input_busqueda = page.get_by_placeholder(
            "Buscar en Wikipedia").first
        self.titulo_principal = page.locator("h1#firstHeading")

    def navegar_a_wikipedia(self):
        print("🌐 Navegando a la página de inicio...")
        self.page.goto("https://es.wikipedia.org/")

    def buscar_tema(self, tema: str):
        print(f"✏️ Escribiendo '{tema}' en el cuadro de búsqueda...")
        self.input_busqueda.fill(tema)
        print("⌨️ Presionando Enter...")
        self.input_busqueda.press("Enter")

    def obtener_titulo_articulo(self) -> str:
        self.titulo_principal.wait_for()
        return self.titulo_principal.inner_text()
