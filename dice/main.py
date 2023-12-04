from enum import Flag, auto

from kivy.app import App
from kivy.uix.widget import Widget


class DieFace(Flag):
    TOP_LEFT = auto()
    MIDDLE_LEFT = auto()
    BOTTOM_LEFT = auto()
    TOP_MIDDLE = auto()
    MIDDLE_MIDDLE = auto()
    BOTTOM_MIDDLE = auto()
    TOP_RIGHT = auto()
    MIDDLE_RIGHT = auto()
    BOTTOM_RIGHT = auto()


class DiceRollView(Widget):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)

    def setup(self) -> None:
        pass


class DiceRollApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.root: DiceRollView

    def build(self):
        self.root = DiceRollView()
        return self.root

    def on_start(self):
        self.root.setup()
