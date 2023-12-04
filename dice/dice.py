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


DIE_ONE = DieFace.MIDDLE_MIDDLE
DIE_TWO = DieFace.TOP_RIGHT | DieFace.BOTTOM_LEFT
DIE_THREE = DieFace.TOP_RIGHT | DieFace.MIDDLE_MIDDLE | DieFace.BOTTOM_LEFT
DIE_FOUR = DieFace.TOP_LEFT | DieFace.TOP_RIGHT | DieFace.BOTTOM_LEFT | DieFace.BOTTOM_RIGHT
DIE_FIVE = DieFace.TOP_LEFT | DieFace.TOP_RIGHT | DieFace.MIDDLE_MIDDLE | DieFace.BOTTOM_LEFT | DieFace.BOTTOM_RIGHT
DIE_SIX = (DieFace.TOP_LEFT | DieFace.TOP_RIGHT | DieFace.MIDDLE_LEFT | DieFace.MIDDLE_RIGHT | DieFace.BOTTOM_LEFT |
           DieFace.BOTTOM_RIGHT)

DIE_FACES = (DIE_ONE, DIE_TWO, DIE_THREE, DIE_FOUR, DIE_FIVE, DIE_SIX)

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


if __name__ == "__main__":
    app = DiceRollApp()
    app.run()
