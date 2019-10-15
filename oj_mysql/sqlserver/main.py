# -*- coding:UTF-8 -*-

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
import kivent_core
from kivy.uix.checkbox import CheckBox
from kivy.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen




class ScreenManager(ScreenManager): 
    pass

class HomeScreen(Screen): 

    def __init__(self,**kwargs):
        super(HomeScreen, self).__init__(**kwargs)

    def on_checkbox_active(self,id):
        checkbox = self.ids[id]
        value = checkbox.active
        if value:
            print('The checkbox', checkbox, 'is active')
        else:
            print('The checkbox', checkbox, 'is inactive')

class AnotherScreen(Screen): 
    pass 

class Sqlserver(App): 
    def build(self): 
        return ScreenManager() 

if __name__ == '__main__':
    Sqlserver().run()

