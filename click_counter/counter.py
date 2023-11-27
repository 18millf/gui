from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.widget import Widget


class CounterView(Widget):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.count: int = 0

        self.count_label: Label = None

    def setup(self) -> None:
        self.count_label = self.ids["counter"]

    def deincrement(self) -> None:
        self.count = max(0, self.count - 1)
        self.update_count()

    def increment(self) -> None:
        self.count += 1 
        # max number is so arbitrarily large, theres not much point clamping it
        self.update_count()

    def update_count(self) -> None:
        self.count_label.text = str(self.count)

class CounterApp(App):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.root: CalculatorView

    def build(self) -> Widget:
        self.root = CounterView()
        return self.root

    def on_start(self) -> None:
        self.root.setup()


if __name__ == "__main__":
    app = CounterApp()
    app.run()
