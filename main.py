# Importar librerías
from kivymd.app import MDApp
from kivy.lang import Builder
from functools import partial
import os.path


# Importar Pantallas
from baseclass.dashboard import DashBoard
from baseclass.settingsscreen import SettingsScreen
from baseclass.pickersscreen import PickersScreen
from baseclass.suggestionsscreen import SuggestionsScreen
from baseclass.streamscreen import StreamScreen
from baseclass.classes import ListIcon


# Inicialización de la APP
class MyApp(MDApp):
    def __init__(self, **kw):
        super().__init__(**kw)
        # Diccionario de pantallas, Pantalla: (id, nombre a mostrar ("text"), icono)
        self.list_screen = {
            DashBoard: ("dashboard", "DashBoard", "view-dashboard"),
            PickersScreen: ("pickers_screen", "Pickers", "calendar-edit"),
            SuggestionsScreen: ("suggestions_screen", "Sugerencias", "account-card-details"),
            StreamScreen: ("stream_screen", "Stream", "video-wireless"),
            SettingsScreen: ("settings_screen", "Ajustes", "settings")
        }

    # Constructor
    def build(self):
        # Ajustes adicionales
        self.title = "Mi Primera App"
        self.theme_cls.primary_palette = "Green"
        # Carga del archivo kivy
        return Builder.load_file('main.kv')

    def on_start(self):
        for screen, details in self.list_screen.items():
            identification, text, icon = details
            kv_file = identification.replace("_", "")
            Builder.load_file(f"kv/{kv_file}.kv")
            self.root.ids.screen_manager.add_widget(screen(name=identification))
            self.root.ids.nav_list.add_widget(ListIcon(text=text, icon=icon,
                                                       on_release=partial(self.button_list_actions,
                                                                          text,
                                                                          identification)))

    def button_list_actions(self, nombre, identification):
        self.title = nombre
        self.root.ids.screen_manager.current = identification
        self.root.ids.nav_drawer.set_state()


if __name__ in ('__main__', '__android__'):
    MyApp().run()
