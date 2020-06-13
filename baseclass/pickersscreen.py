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
        min_date = datetime.strptime("2020:05:11", '%Y:%m:%d').date()
        max_date = datetime.strptime("2020:05:17", '%Y:%m:%d').date()
        date_dialog = MDDatePicker(
            callback=self.get_date,
            min_date=min_date,
            max_date=max_date,
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
