from kivy.uix.screenmanager import Screen
from database import db

class LoginScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    #  Validate username and password
    def validate(self):
        username = self.ids.username.text
        password = self.ids.password.text
        result = db.check_user(username, password)
        if not result:
            self.display_error(username, password)
        return result

    def display_error(self, username, password):
        if username != '':
            error_message1 = 'Incorrect username'
            self.ids.username.helper_text = error_message1
            self.ids.username.error = True
        else:
            error_message = 'This field is required'
            self.ids.username.helper_text = error_message
            self.ids.username.error = True

        if password != '':
            error_message2 = 'Incorrect password'
            self.ids.password.helper_text = error_message2
            self.ids.password.error = True
        else:
            error_message = 'This field is required'
            self.ids.password.helper_text = error_message
            self.ids.password.error = True


    def clear_username(self):
        self.ids.username.text = ''

    def clear_password(self):
        self.ids.password.text = ''

