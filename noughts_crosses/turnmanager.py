from typing import TypeVar, Generic

T = TypeVar("T")

class TurnManager(Generic[T]):
    def __init__(self, turns: list(T)) -> None:
        self.__turns: list(T) = turns
        self.__current_turn: int = 0
        self.__turn_count = len(self.__turns)

    def get_current_turn(self) -> T:
        return self.__turns[self.__current_turn % self.__turn_count]
    
    def advance_turn(self) -> None:
        self.__current_turn += 1