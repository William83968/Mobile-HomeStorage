from kivy.uix.screenmanager import Screen
from kivy.clock import Clock
from datetime import datetime
from kivy.uix.boxlayout import BoxLayout

class HomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update_time, 1)

    def update_time(self, *args):
        now = datetime.now()
        current_time = now.strftime("%-I:%M:%S")
        self.ids.time_label.text = current_time

    def display_menu(self, button):
        print(button)


    