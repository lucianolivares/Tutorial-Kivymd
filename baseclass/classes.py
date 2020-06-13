from kivymd.app import MDApp
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.button import MDIconButton, MDFillRoundFlatIconButton
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivy.uix.textinput import TextInput
from kivy.graphics import Color, RoundedRectangle
from kivy.uix.image import Image
import kivy.utils


class Suggestions(FloatLayout):
    # Clase encargada de crear y rellenar el layout que se agregara como slide a Carousel
    def __init__(self, **kw):
        super().__init__()
        self.pos_hint = {"x": .1, "y": .1}
        self.size_hint = .8, .8

        with self.canvas.before:
            Color(rgba=(0, .4, 0, 0.1))
            self.rect = RoundedRectangle(radius=[(20, 20)])
        self.bind(pos=self.update_rect, size=self.update_rect)

        self.name = MDLabel(text=kw["name"],
                            pos_hint={"center_x": .5, "top": .9}, size_hint=(.5, .1),
                            font_style="H4", halign="center")

        self.image = Image(pos_hint={"center_x": .5, "center_y": .5}, size_hint=(.5, .5),
                           source=kw["source"])

        self.add_button = MDFillRoundFlatIconButton(pos_hint={"right": 1, "y": 0},
                                                    text="Añadir a Contactos", icon="account-plus",
                                                    on_release=kw["add_button_action"])

        self.delete_button = MDIconButton(icon="close", pos_hint={"x": 0, "top": 1}, on_release=kw["on_release"])

        self.add_widget(self.name)
        self.add_widget(self.image)
        self.add_widget(self.add_button)
        self.add_widget(self.delete_button)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size


class ListIcon(OneLineIconListItem):
    def __init__(self, **kw):
        super().__init__()
        self.text = kw["text"]
        self.icon = IconLeftWidget(icon=kw["icon"])
        self.add_widget(self.icon)
        self.on_release = kw["on_release"]


class Banner(FloatLayout):
    def __init__(self, **kwargs):
        super().__init__()

        with self.canvas.before:
            Color(rgba=(0, .4, 0, 0.1))
            self.rect = RoundedRectangle(radius=[(40.0, 40.0), (40.0, 40.0), (40.0, 40.0), (40.0, 40.0)])
        self.bind(pos=self.update_rect, size=self.update_rect)

        self.operation = kwargs["operation"]

        self.title = MDLabel(text=kwargs["title"],
                             pos_hint={"center_x": .5, "top": .9}, size_hint=(.5, .3),
                             theme_text_color="Primary", font_style="H6", halign="center")
        self.text_field = MDTextFieldRect(pos_hint={"center_x": .25, "center_y": .4}, size_hint=(.20, .20),
                                          hint_text="Ingresar Valor", halign="center")
        self.button = MDIconButton(on_release=self.ejecutar,
                                   pos_hint={"center_x": .5, "center_y": .4}, size_hint=(.2, .3),
                                   icon="arrow-right-bold")
        self.result = MDLabel(pos_hint={"center_x": .75, "center_y": .4}, size_hint=(.2, .5),
                              halign="center")

        self.add_widget(self.title)
        self.add_widget(self.text_field)
        self.add_widget(self.button)
        self.add_widget(self.result)

    def ejecutar(self, widget):
        if self.operation == "binary":
            self.is_binary(self.text_field.text)
        elif self.operation == "count_vowels":
            self.count_vowels(self.text_field.text)
        elif self.operation == "is_leap":
            self.is_leap(self.text_field.text)
        elif self.operation == "is_palindrome":
            self.is_palindrome(self.text_field.text)
        elif self.operation == "inverse":
            self.inversa(self.text_field.text)

    def is_binary(self, binary_number):
        try:
            decimal = int(binary_number, 2)
            self.result.text = f'{decimal}'
            self.result.theme_text_color = "Primary"
        except ValueError:
            self.result.text = "Número Incorrecto"
            self.result.theme_text_color = "Error"

    def count_vowels(self, word):
        vocals = ["a", "e", "i", "o", "u"]
        count = 0
        for w in word:
            for v in vocals:
                if w == v:
                    count += 1
        self.result.text = str(count)

    def is_leap(self, year):
        try:
            temp = int(year)
            if temp % 4 == 0 and (not (temp % 100 == 0)) or temp % 400 == 0:
                self.result.text = "Es Bisiesto"
                self.result.theme_text_color = "Primary"
            else:
                self.result.text = "NO es Bisiesto"
                self.result.theme_text_color = "Primary"
        except ValueError:
            self.result.text = "Valor ingresado invalido"
            self.result.theme_text_color = "Error"

    def is_palindrome(self, string):
        temp = ""
        largo = len(string)
        for i in range(largo):
            ind = -1
            ind -= i
            temp += string[ind]
            if temp == string:
                self.result.text = "Es palíndromo"
            else:
                self.result.text = "NO es palíndromo"

    def inversa(self, string):
        temp = ""
        largo = len(string)
        for i in range(largo):
            ind = -1
            ind -= i
            temp += string[ind]
        self.result.text = str(temp)

    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
