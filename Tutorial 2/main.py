# Importar librerías
from kivymd.app import MDApp
from kivy.lang import Builder


# Importar Pantallas
from baseclass.dashboard import DashBoard
from baseclass.settingsscreen import SettingsScreen


# Inicialización de la APP
class MyApp(MDApp):

    # Constructor
    def build(self):
        # Ajustes adicionales
        self.title = "Mi Primera App"
        self.theme_cls.primary_palette = "Green"
        # Carga del archivo kivy
        return Builder.load_file("main.kv")


# Ejecutar App
MyApp().run()
