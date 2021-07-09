from re import MULTILINE
from typing import MutableMapping, Text
from kivy.app import App
from kivy.core.text import FONT_BOLD
from kivy.uix.behaviors import button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.cols = 1;

        self.inside = GridLayout()
        self.inside.cols = 2;

        self.inside.add_widget(Label(text='Name:'))
        self.name = TextInput(multiline=False)
        self.inside.add_widget(self.name)

        self.inside.add_widget(Label(text="Last Name:"))
        self.lastname = TextInput(multiline=False)
        self.inside.add_widget(self.lastname)

        self.add_widget(self.inside)
        self.submit = Button(text="submit",font_size=20)
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    
    def press(self,instance):

        name = self.name.text
        last = self.lastname.text


        print("Name: ",name,"Last Name: ",last)
        self.name.text = ''
        self.lastname.text = ''




class TestApp(App):
    def build(self):
        return MyGrid()        

if __name__ == "__main__":
    TestApp().run()