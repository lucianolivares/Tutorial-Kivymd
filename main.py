from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


from baseclass.dashboard import DashBoard
from baseclass.settingsscreen import SettingsScreen
from baseclass.pickersscreen import PickersScreen
from baseclass.suggestionsscreen import SuggestionsScreen


class MyApp(MDApp):
    def build(self):
        self.title = ""
        self.theme_cls.primary_palette = "Green"
        return Builder.load_file("main.kv")


MyApp().run()
