import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout


class Calculator(App):
    def build(self):
        layout = GridLayout(cols=4, spacing=10)  # Added spacing for better visualization

        
        # Create a BoxLayout for the display screen
        screen_layout = BoxLayout(orientation='horizontal', size_hint=(None, 0.2))
        self.display = Label(text='', font_size=40, halign='right', valign='middle')
        screen_layout.add_widget(self.display)
        layout.add_widget(screen_layout)


        # Add buttons in the desired order
        layout.add_widget(Button(text='clear'))
        layout.add_widget(Button(text='del'))
        layout.add_widget(Button(text='%'))
        layout.add_widget(Button(text='/'))

        for i in range(7, 10):
            layout.add_widget(Button(text=str(i)))
        layout.add_widget(Button(text='*'))

        for i in range(4, 7):
            layout.add_widget(Button(text=str(i)))
        layout.add_widget(Button(text='-'))

        for i in range(1, 4):
            layout.add_widget(Button(text=str(i)))
        layout.add_widget(Button(text='+'))

        layout.add_widget(Button(text='pass'))
        layout.add_widget(Button(text='0'))
        layout.add_widget(Button(text='.'))
        layout.add_widget(Button(text='='))

        return layout

if __name__ == '__main__':
    Calculator().run()