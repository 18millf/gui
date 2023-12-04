from enum import Flag, auto


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

