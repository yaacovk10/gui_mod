import kivy
from kivy.app import App
from kivy.uix.button import Button

# Define the main application class
class MyApp(App):
    def build(self):
        # Create a button widget
        button = Button(text="Click Me!")

        # Bind the button to a function to handle the click event
        button.bind(on_press=self.on_button_click)

        # Return the button as the root widget for the application
        return button

    # Function to handle the button click event
    def on_button_click(self, instance):
        print("Button clicked!")


import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.graphics import Color, Rectangle

class ColorChangeApp(App):
    def build(self):
        # Create a layout for the buttons
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Create blue button
        blue_button = Button(text="Blue")
        blue_button.bind(on_press=lambda instance: self.change_color(instance, (0, 0, 1, 1)))

        # Create green button
        green_button = Button(text="Green")
        green_button.bind(on_press=lambda instance: self.change_color(instance, (0, 1, 0, 1)))

        # Create red button
        red_button = Button(text="Red")
        red_button.bind(on_press=lambda instance: self.change_color(instance, (1, 0, 0, 1)))

        # Add buttons to the layout
        layout.add_widget(blue_button)
        layout.add_widget(green_button)
        layout.add_widget(red_button)

        return layout

    def change_color(self, instance, color):
        # Change the button's background color
        instance.background_color = color
    


# Run the Kivy application
if __name__ == '__main__':
    # MyApp().run()
    ColorChangeApp().run()
