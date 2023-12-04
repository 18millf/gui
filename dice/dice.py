from enum import Flag, auto
from random import randrange

from kivy.app import App
from kivy.uix.label import Label
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


def has_flag(value: Flag, flag: Flag) -> bool:
    return value & flag == flag


DIE_ONE: DieFace = DieFace.MIDDLE_MIDDLE
DIE_TWO: DieFace = DieFace.TOP_RIGHT | DieFace.BOTTOM_LEFT
DIE_THREE: DieFace = DieFace.TOP_RIGHT | DieFace.MIDDLE_MIDDLE | DieFace.BOTTOM_LEFT
DIE_FOUR: DieFace = DieFace.TOP_LEFT | DieFace.TOP_RIGHT | DieFace.BOTTOM_LEFT | DieFace.BOTTOM_RIGHT
DIE_FIVE: DieFace = DieFace.TOP_LEFT | DieFace.TOP_RIGHT | DieFace.MIDDLE_MIDDLE | DieFace.BOTTOM_LEFT | DieFace.BOTTOM_RIGHT
DIE_SIX: DieFace = (
            DieFace.TOP_LEFT | DieFace.TOP_RIGHT | DieFace.MIDDLE_LEFT | DieFace.MIDDLE_RIGHT | DieFace.BOTTOM_LEFT |
            DieFace.BOTTOM_RIGHT)

DIE_FACES = (DIE_ONE, DIE_TWO, DIE_THREE, DIE_FOUR, DIE_FIVE, DIE_SIX)

FILL_CHAR: str = "•"


class DiceRollView(Widget):
    def __init__(self, **kwargs) -> None:
        super().__init__(**kwargs)
        self.top_left: Label = None
        self.middle_left: Label = None
        self.bottom_left: Label = None
        self.top_middle: Label = None
        self.middle_middle: Label = None
        self.bottom_middle: Label = None
        self.top_right: Label = None
        self.middle_right: Label = None
        self.bottom_right: Label = None

    def setup(self) -> None:
        self.top_left = self.ids["top_left"]
        self.middle_left = self.ids["middle_left"]
        self.bottom_left = self.ids["bottom_left"]
        self.top_middle = self.ids["top_middle"]
        self.middle_middle = self.ids["middle_middle"]
        self.bottom_middle = self.ids["bottom_middle"]
        self.top_right = self.ids["top_right"]
        self.middle_right = self.ids["middle_right"]
        self.bottom_right = self.ids["bottom_right"]

    def set_face(self, face: DieFace) -> None:
        if has_flag(face, DieFace.TOP_LEFT):
            self.top_left.text = FILL_CHAR
        if has_flag(face, DieFace.MIDDLE_LEFT):
            self.middle_left.text = FILL_CHAR
        if has_flag(face, DieFace.BOTTOM_LEFT):
            self.bottom_left.text = FILL_CHAR
        if has_flag(face, DieFace.TOP_MIDDLE):
            self.top_middle.text = FILL_CHAR
        if has_flag(face, DieFace.MIDDLE_MIDDLE):
            self.middle_middle.text = FILL_CHAR
        if has_flag(face, DieFace.BOTTOM_MIDDLE):
            self.bottom_middle.text = FILL_CHAR
        if has_flag(face, DieFace.TOP_RIGHT):
            self.top_right.text = FILL_CHAR
        if has_flag(face, DieFace.MIDDLE_RIGHT):
            self.middle_right.text = FILL_CHAR
        if has_flag(face, DieFace.BOTTOM_RIGHT):
            self.bottom_right.text = FILL_CHAR

    def reset_face(self) -> None:
        self.top_left.text = ""
        self.middle_left.text = ""
        self.bottom_left.text = ""
        self.top_middle.text = ""
        self.middle_middle.text = ""
        self.bottom_middle.text = ""
        self.top_right.text = ""
        self.middle_right.text = ""
        self.bottom_right.text = ""

    def roll(self):
        self.reset_face()
        result: int = randrange(0, 6)
        self.set_face(DIE_FACES[result])


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
