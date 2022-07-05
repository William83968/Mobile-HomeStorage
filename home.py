from kivymd.uix.screen import MDScreen
from kivymd.uix.button import MDFloatingActionButtonSpeedDial
from datetime import datetime
from kivy.clock import Clock
from database import db
import pytz

class HomeScreen(MDScreen):
    data = {
            'Lua':'language-lua',
            'Python':'language-python',
            'Rust':'language-rust'
        }
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_interval(self.update, 1)


    def update(self, *args):
        timezone = pytz.timezone(db.country+'/'+db.city)
        now = datetime.now(timezone)
        current_time = now.strftime("%-I:%M:%S")
        self.ids.time_label.text = current_time