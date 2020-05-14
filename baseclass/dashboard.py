from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

from baseclass.banner import Banner


class DashBoard(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.app = MDApp.get_running_app()

    def on_pre_enter(self, *args):
        self.app.title = "Dash Board"

    def on_kv_post(self, base_widget):
        # Rellenar ScrollView con banners
        grid = self.ids["grid_banner"]
        # Indicamos la operación y el título
        operations = {"binary": "Convertidor de Números Binario",
                      "count_vowels": "Contador de Vocales",
                      "is_leap": "Comprobar Año Bisiesto",
                      "is_palindrome": "Verificador de Palíndromo",
                      "inverse": "Invertir Sentencia"
                      }

        for operation, title in operations.items():
            banner = Banner(operation=operation, title=title)
            grid.add_widget(banner)
