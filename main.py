# Import kivy core modules
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivymd.app import MDApp

# Import kivy components
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.list.list import MDList, OneLineIconListItem

# Import other stuff
from kivymd.theming import ThemableBehavior
from kivy.properties import StringProperty
import pytz
import os

# Import screens
from home import HomeScreen
from signup import SignupScreen
from categories import CategoriesScreen
from houses import HousesScreen
from items import ItemsScreen
from login import LoginScreen
from user import UserScreen

class ContentNavigationDrawer(BoxLayout):
    pass

class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()

class DrawerList(ThemableBehavior, MDList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Clock.schedule_once(self.on_start, 0)

    def set_color_item(self, instance_item):
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color = self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color

    def on_start(self, *args):
        icons_item = {
            "home": "Home",
            "folder-home": "Houses",
            "format-list-bulleted": "Categories",
            "blur-linear": "Item",
            "account": "User"
        }
        for icon_name in icons_item.keys():
            self.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )

class ScreenManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class MainScreen(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        screens = [LoginScreen(name='LoginScreen'),
                    SignupScreen(name='SignupScreen'),
                    HomeScreen(name='HomeScreen'),
                    HousesScreen(name='HousesScreen'),
                    CategoriesScreen(name='CategoriesScreen'),
                    ItemsScreen(name='ItemsScreen'),
                    UserScreen(name='UserScreen')]
        for screen_name in screens:
            self.ids.WindowManager.add_widget(screen_name)

# Configurations
class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Cyan"
        self.theme_cls.accent_palette = "BlueGray"
        Window.size = (1366, 1024)
        return MainScreen()

if __name__ == '__main__':
   MainApp().run()