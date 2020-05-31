from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.uix.picker import MDDatePicker, MDTimePicker, MDThemePicker
from datetime import datetime


class PickersScreen(Screen):

    def get_date(self, date):
        self.ids["fecha"].text = date.strftime("%d/%m/%Y")

    def get_time(self, instance, time):
        self.ids["hora"].text = time.strftime("%H:%M")

    def show_date_picker(self):
        min_date = datetime.strptime("11:05:2020", "%d:%m:%Y").date()
        max_date = datetime.strptime("17:05:2020", "%d:%m:%Y").date()

        date_dialog = MDDatePicker(
            callback=self.get_date,
            min_date=min_date,
            max_date=max_date
        )
        date_dialog.open()

    def show_time_picker(self):
        """Open time picker dialog."""
        time_dialog = MDTimePicker()
        time_dialog.bind(time=self.get_time)
        time_dialog.open()

    @staticmethod
    def show_theme_picker():
        theme_dialog = MDThemePicker()
        theme_dialog.open()
