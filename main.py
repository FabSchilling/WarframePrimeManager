from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

class MenuScreen(Screen):
    pass

class SettingsScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))

class WarframePrimeManagerApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    WarframePrimeManagerApp().run()