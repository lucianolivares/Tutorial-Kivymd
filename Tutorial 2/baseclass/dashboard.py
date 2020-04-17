from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp


class DashBoard(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = MDApp.get_running_app()
        self.sub_title = "Convertidor de números binarios"
        self.hint_binary_number = "Ingresar un número binario"

    def on_enter(self, *args):
        self.app.title = "Dash Board"

    def is_binary(self, binary_number):
        try:
            decimal = int(binary_number, 2)
            self.ids["solution"].text = f'Resultado: {decimal}'
            self.ids["solution"].theme_text_color = "Primary"
        except ValueError:
            self.ids["solution"].text = "Número Incorrecto"
            self.ids["solution"].theme_text_color = "Error"
