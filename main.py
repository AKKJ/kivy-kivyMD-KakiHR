# https://www.youtube.com/watch?v=_pwbZofoffI
# incomplete 200423
# $env:DEBUG = 1; python main.py

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.factory import Factory as F
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from datetime import datetime
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button

Window.size = 360, 640


class StackLayoutEx(StackLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        for i in range (0, 10):
            b = Button(text=str(i), size_hint=(0.2, 0.2))
            self.add_widget(b)

class main(MDApp):
    pass

if __name__ == "__main__":
    main().run()