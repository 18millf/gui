import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
import threading
import time
from random import random

def reset_color(btn: Button):
    btn.background_color = [1, 1, 1, 1]

class Application(App):
    def build(self):
        main_layout = BoxLayout(orientation="vertical")
        action_button = Button(text="GO!")
        main_layout.add_widget(action_button)

        button_grid = GridLayout(cols=5, rows=5)

        buttons: list(Button) = []
        for _ in range(25):
            new_button: Button = Button()
            button_grid.add_widget(new_button)
            buttons.append(new_button)
            new_button.on_press = lambda self: reset_color(self)

        main_layout.add_widget(button_grid)

        def callback():
            for button in buttons:
                button.background_color = [random(), random(), random(), 1]
                

        action_button.on_press = lambda: threading.Thread(target=callback).run()

        return main_layout
        
    
if __name__ == "__main__":
    app = Application()
    app.run()