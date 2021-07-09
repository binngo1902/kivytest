from kivy.app import App 
from kivy.uix.floatlayout import FloatLayout



from kivy.app import App


class Test2App(App):
    def build(self):
        return FloatLayout()


def main():
    Test2App().run()


if __name__ == '__main__':
    main()