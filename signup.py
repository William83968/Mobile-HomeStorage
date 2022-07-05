from kivy.lang import Builder
from kivymd.uix.screen import MDScreen
from database import db

class SignupScreen(MDScreen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def signup(self):
        # setup variables
        self.username = self.ids.username
        self.password = self.ids.password
        self.optional_fields = [self.ids.email,
                                self.ids.address,
                                self.country,
                                self.city]
        # appending data according to the text field
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

        print(datas)

        # db.user_submit(datas)
        # return True

    def clear(self):
        self.ids.username.text = ''
        self.ids.username.text = ''
        self.ids.email.text = ''
        self.ids.address.text = ''
        self.ids.country.text = ''
        self.ids.city.text = ''
