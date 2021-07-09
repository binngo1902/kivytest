from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        self.operators = ['/','+','-','*']
        self.last_was_operator = None
        self.last_button = None

        #  Dựng một khung chính
        main_layout = BoxLayout(orientation='vertical')
        
        #  Tạo dòng hiển thị số nhập, phép tính
        self.display = TextInput(multiline=False,readonly=True,halign="right",font_size=50)
        main_layout.add_widget(self.display)

        # tạo các button 

        buttons = [
            ['7','8','9','/'],
            ['4','5','6','*'],
            ['1','2','3','+'],
            ['.','0','C','-'],
        ]

        for row in buttons:
            row_button = BoxLayout()
            for label in row:
                button = Button(text=label,size_hint=(1,1),font_size=50)
                button.bind(on_press=self.press_button)
                row_button.add_widget(button)
            main_layout.add_widget(row_button)
            
        equal_button = Button(text="=",font_size=50)
        equal_button.bind(on_press=self.equal)
        main_layout.add_widget(equal_button)
        return main_layout

    def press_button(self,value):
        current = self.display.text # đọc giá trị đang hiển thị
        button_text = value.text # đọc giá trị của nút vừa nhấn 

        if button_text == "C": # vừa nhấn nút là C thì delete
            self.display.text = ""
        else:
            if current == '' and ((button_text in self.operators) or button_text == "."): # check display rỗng và nút vừa nhấn là phép tính
                # check display rỗng và nút bắt đầu là operator hoặc dấu chấm
                return 
            
            if (button_text in self.operators) and self.last_was_operator :
                # check xem nút vừa nhấn là phép tính và nút đã nhấn trước có phải phép tính không
                return 
            if (button_text == '.') and (self.last_was_operator or self.last_button == "."):
                # check xem dấu . và phép toán trước đó hoặc nút trước là dấu chấm 
                return
            if (self.last_button == "=") and (button_text == "."):
                # check xem nhấn lần trước là dấu = và nút vừa nhấn là dấu . 
                return
            if (self.last_button == "=") and (button_text not in self.operators):
                self.last_button = button_text
                self.display.text = button_text
                return
            if (self.last_button == "0") and button_text != ".":
                return
            
            self.display.text = current+button_text

           
        self.last_button = button_text

        # nếu nút vừa nhấn nằm trong operator thì trả về true không thì false
        self.last_was_operator = self.last_button in self.operators 

    def equal(self,value):
        text = self.display.text # lấy nội dung của display 
        if self.last_button in self.operators:
            return 
        else:
            equal = str(eval(text)) # hàm eval để tính và ép kiểu thành str
            self.display.text = equal
        self.last_button = value.text # lưu phím = vào last_button


def main():
    MainApp().run()


if __name__ == '__main__':
    main()