import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class Calculator(App):
    def build(self):
        layout = GridLayout(cols=1, spacing=10)  # Main layout with a single column

        # Create a GridLayout for the display screen and buttons in each row
        screen_layout = GridLayout(cols=4, size_hint_y=None, height=100, spacing=10)
        self.display = Label(text='', font_size=40, halign='right', valign='middle')
        screen_layout.add_widget(self.display)
        layout.add_widget(screen_layout)

        # Add buttons in the desired order
        layout_buttons = GridLayout(cols=4, spacing=10)

        layout_buttons.add_widget(Button(text='clear', on_press=self.on_button_press))
        layout_buttons.add_widget(Button(text='del', on_press=self.on_button_press))
        layout_buttons.add_widget(Button(text='%', on_press=self.on_button_press))
        layout_buttons.add_widget(Button(text='/', on_press=self.on_button_press))

        for i in range(7, 10):
            layout_buttons.add_widget(Button(text=str(i), on_press=self.on_button_press))
        layout_buttons.add_widget(Button(text='*', on_press=self.on_button_press))

        for i in range(4, 7):
            layout_buttons.add_widget(Button(text=str(i), on_press=self.on_button_press))
        layout_buttons.add_widget(Button(text='-', on_press=self.on_button_press))

        for i in range(1, 4):
            layout_buttons.add_widget(Button(text=str(i), on_press=self.on_button_press))
        layout_buttons.add_widget(Button(text='+', on_press=self.on_button_press))

        layout_buttons.add_widget(Button(text='pass', on_press=self.on_button_press))
        layout_buttons.add_widget(Button(text='0', on_press=self.on_button_press))
        layout_buttons.add_widget(Button(text='.', on_press=self.on_button_press))
        layout_buttons.add_widget(Button(text='=', on_press=self.on_button_press))

        layout.add_widget(layout_buttons)

        return layout

    def on_button_press(self, instance):
        current_text = self.display.text
        button_text = instance.text

        if button_text == 'clear':
            self.display.text = ''
        elif button_text == 'del':
            self.display.text = current_text[:-1]
        elif button_text == '%':
            res = self.operation
            self.display.text = str(eval(res/100))
        elif button_text == '=':
            self.display.text = self.operation(current_text)
        else:
            self.display.text += button_text

    def operation(self, current_text):
        try:
            return str(eval(current_text))
        except Exception as e:
            return 'Error'

if __name__ == '__main__':
    Calculator().run()
