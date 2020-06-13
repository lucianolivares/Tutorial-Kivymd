from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp

from baseclass.classes import Banner


class DashBoard(Screen):
    def on_kv_post(self, base_widget):
        grid = self.ids["grid_banner"]
        operations = {"binary": "Convertidor de Números Binario",
                      "count_vowels": "Contador de Vocales",
                      "is_leap": "Comprobar Año Bisiesto",
                      "is_palindrome": "Verificador de Palíndromo",
                      "inverse": "Invertir Sentencia"
                      }
        for operation, title in operations.items():
            banner = Banner(title=title, operation=operation)
            grid.add_widget(banner)
