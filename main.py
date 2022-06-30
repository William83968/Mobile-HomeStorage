from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, WipeTransition, Screen
from login import LoginScreen
from home import HomeScreen
from signup import SignupScreen

class ContentNavigationDrawer(BoxLayout):
    pass

class ScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
 
# Configurations
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark" 
        self.theme_cls.primary_palette = "Cyan" 
        self.theme_cls.accent_palette = "BlueGray"
        Window.size = (1366, 1024)
        return MainScreen()

if __name__ == '__main__':
    MainApp = MainApp()
    MainApp.run()