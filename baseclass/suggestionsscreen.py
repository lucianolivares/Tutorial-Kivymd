from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, RoundedRectangle
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDFillRoundFlatIconButton, MDIconButton
from kivy.uix.image import Image


class Suggestions(FloatLayout):
    # Clase encargada de crear y rellenar el layout que se agregara como slide a Carousel
    def __init__(self, **kwargs):
        super().__init__()
        self.pos_hint = {"x": .1, "y": .1}
        self.size_hint = .8, .8

        with self.canvas.before:
            Color(rgba=(0, .4, 0, 0.1))
            self.rect = RoundedRectangle(radius=[(20, 20)])
        self.bind(pos=self.update_rect, size=self.update_rect)

        self.name = MDLabel(text=kwargs["name"],
                            pos_hint={"center_x": .5, "top": .9}, size_hint=(.5, .1),
                            font_style="H4", halign="center")

        self.image = Image(pos_hint={"center_x": .5, "center_y": .5}, size_hint=(.5, .5),
                           source=kwargs["source"])

        self.add_button = MDFillRoundFlatIconButton(pos_hint={"right": 1, "y": 0},
                                                    text="Añadir a Contactos", icon="account-plus")

        self.delete_button = MDIconButton(icon="close", pos_hint={"x": 0, "top": 1}, on_release=kwargs["on_release"])

        self.add_widget(self.name)
        self.add_widget(self.image)
        self.add_widget(self.add_button)
        self.add_widget(self.delete_button)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class SuggestionsScreen(Screen):
    carousel: object

    def __init__(self, **kw):
        super().__init__(**kw)
        self.app = MDApp.get_running_app()

        self.sugerencias = {
            "Carlos Contador": "people-1.jpg",
            "Carla Herrera": "people-2.jpg",
            "Rocío Perez": "people-3.jpg",
            "Felipe Rojas": "people-4.jpg"
        }

    def on_kv_post(self, base_widget):
        self.carousel = self.ids["suggestions_carousel"]
        for name, imagen in self.sugerencias.items():
            tarjeta = Suggestions(name=name, source=f"resources/{imagen}", on_release=self.my_callback)
            self.carousel.add_widget(tarjeta)

    def my_callback(self, widget):

        if self.carousel.current_slide is self.carousel.slides[-1]:
            self.carousel.remove_widget(self.carousel.current_slide)
            self.carousel.load_previous()
            if not self.carousel.slides:
                self.carousel.add_widget(MDLabel(font_style="H3", text="No tienes más sugerencias", halign="center"))
        else:
            self.carousel.remove_widget(self.carousel.current_slide)

    def on_pre_enter(self, *args):
        self.app.title = "Sugerencias"
