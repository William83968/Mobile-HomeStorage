from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.theming import ThemableBehavior
from kivymd.uix.list.list import MDList, OneLineIconListItem, IconLeftWidget
from kivymd.uix.navigationdrawer.navigationdrawer import MDNavigationLayout, MDNavigationDrawerItem
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from home import HomeScreen

class ContentNavigationDrawer(BoxLayout):
    pass

class DrawerList(ThemableBehavior, MDList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

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