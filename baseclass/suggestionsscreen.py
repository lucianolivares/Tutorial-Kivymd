from typing import Dict

from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, RoundedRectangle
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatIconButton, MDIconButton
from kivy.uix.image import Image

from baseclass.classes import Suggestions


class SuggestionsScreen(Screen):
    sugerencias: Dict[str, str]
    carousel: object

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = MDApp.get_running_app()

    def on_kv_post(self, base_widget):
        self.sugerencias = {
            "Carlos Contador": "people-1.jpg",
            "Carla Herrera": "people-2.jpg",
            "Rocío Perez": "people-3.jpg",
            "Felipe Rojas": "people-4.jpg"
        }
        self.carousel = self.ids["suggestions_carousel"]
        for nombre, imagen in self.sugerencias.items():
            tarjeta = Suggestions(name=nombre, source=f"resources/{imagen}", on_release=self.my_callback,
                                  add_button_action=self.change_screen)

            self.carousel.add_widget(tarjeta)

    def my_callback(self, widget):
        self.sugerencias.pop(self.carousel.current_slide.name.text)
        if self.carousel.current_slide is self.carousel.slides[-1]:
            self.carousel.remove_widget(self.carousel.current_slide)
            self.carousel.load_previous()
            if not self.carousel.slides:
                self.carousel.add_widget(MDLabel(font_style="H3", text="No tienes más sugerencias", halign="center"))
        else:
            self.carousel.remove_widget(self.carousel.current_slide)

    def change_screen(self, widget):
        self.app.root.ids.screen_manager.current = "dashboard"
        self.app.title = "DashBoard"
