from re import MULTILINE
from typing import MutableMapping, Text
from kivy.app import App
from kivy.core.text import FONT_BOLD
from kivy.uix.behaviors import button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
class MyGrid(Widget):
    name = ObjectProperty(None)
    lastname = ObjectProperty(None)
    
    def btn(self):
        print('Name: ',self.name.text,"last Name: ",self.lastname.text)
        self.name.text =''
        self.lastname.text =''



class TestApp(App):
    def build(self):
        return MyGrid()  
              

if __name__ == "__main__":
    TestApp().run()