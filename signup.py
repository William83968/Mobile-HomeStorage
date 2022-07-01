from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from database import db
from kivy.clock import Clock

class SignupScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.startup, 0)

    def startup(self, *args):
        self.username = self.ids.username
        self.password = self.ids.password
        self.optional_fields = [self.ids.email,
                self.ids.address,
                self.ids.city]

    def signup(self):
        datas = []
        if self.username.text == '' or self.password.text == '':
            if self.username.text == '':
                self.username.error = True
            if self.password.text == '':
                self.password.error = True
            return False
        else:
            datas.append(self.username.text)
            datas.append(self.password.text)

        for d in self.optional_fields:
            if d.text == '':
                datas.append('')
            else:
                datas.append(d.text)

        db.user_submit(datas)
        return True

    def clear(self):
        self.username.text = ''
        self.password.text = ''
        for d in self.optional_fields:
            d.text = ''
