from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.widget import Widget

NINE_FIFTHS: float = 9/5
FIVE_NINETHS: float = 5/9

class ConverterView(Widget):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.celsius: TextInput = None
        self.farenheit: TextInput = None

    def setup(self) -> None:
        self.celsius = self.ids["celsius_text"]
        self.farenheit = self.ids["farenheit_text"]

        self.celsius.text = "0"
        self.celsius_to_farenheit()

    # Temperature in degrees Fahrenheit (°F) 
    # = (Temperature in degrees Celsius (°C) * 9/5) + 32.

    def celsius_to_farenheit(self) -> None:
        c: float = float(self.celsius.text)
        f: float = (c * NINE_FIFTHS) + 32
        self.farenheit.text = str(f)

    def farenheit_to_celsius(self) -> None:
        f: float = float(self.farenheit.text)
        c: float = (f - 32) * FIVE_NINETHS
        self.celsius.text = str(c)


class ConverterApp(App):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.root: ConverterView

    def build(self) -> Widget:
        self.root = ConverterView()
        return self.root

    def on_start(self):
        self.root.setup()

if __name__ == "__main__":
    ConverterApp().run()
