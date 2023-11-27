from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.uix.widget import Widget


class CalculatorView(Widget):

    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

        self.left_input: TextInput = None
        self.right_input: TextInput = None
        self.result_text: Label = None

    def setup(self) -> None:
        self.left_input = self.ids["left_input"]
        self.right_input = self.ids["right_input"]
        self.result_text = self.ids["result_text"]

    def perform_add(self) -> None:
        left = int(self.left_input.text)
        right = int(self.right_input.text)
        self.set_result(str(left + right))

    def perform_subtract(self) -> None:
        left = int(self.left_input.text)
        right = int(self.right_input.text)
        self.set_result(str(left - right))

    def perform_multiply(self) -> None:
        left = int(self.left_input.text)
        right = int(self.right_input.text)
        self.set_result(str(left * right))

    def perform_divide(self) -> None:
        left = int(self.left_input.text)
        right = int(self.right_input.text)

        if right == 0:
            self.set_result("Cannot divide by zero.")
            return

        self.set_result(str(left // right))

    def set_result(self, result: str) -> None:
        self.result_text.text = f"Result: {result}"



class CalculatorApp(App):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.root: CalculatorView

    def build(self) -> Widget:
        self.root = CalculatorView()
        return self.root

    def on_start(self) -> None:
        self.root.setup()


if __name__ == "__main__":
    app = CalculatorApp()
    app.run()
