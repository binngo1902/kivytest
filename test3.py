from kivy.app import App 
from kivy.uix.button import Button
from kivy.uix.widget import Widget

from kivy.properties import ObjectProperty

class Touch(Widget):
    btn = ObjectProperty(None)

    def on_touch_down(self, touch):
        print('Mouse down',touch)
        self.btn.opacity = 0.5
    def on_touch_move(self, touch):
        print('Mouse move',touch)

    def on_touch_up(self, touch):
        print('mouse up',touch)
        self.btn.opacity= 1


class touchApp(App):
    def build(self):
        return Touch() 


def main():
    touchApp().run()


if __name__ == '__main__':
    main()