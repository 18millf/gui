from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

from game import Game, Placement
from turnmanager import TurnManager

class GameView(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.__game: Game = Game()
        self.__turn_manager = TurnManager([Placement.NOUGHT, Placement.CROSS])
        self.__buttons: list[Button] = list()

        self.orientation = "vertical"

        self.__dialogue: Label = Label()
        self.add_widget(self.__dialogue)

        grid: GridLayout = GridLayout()
        self.add_widget(grid)
        grid.cols = 3

        for row in range(3):
            for column in range(3):
                button: Button = Button()
                button.bind(on_press=self.create_button_callback(row, column))
                button.font_size = 32
                grid.add_widget(button)
                self.__buttons.append(button)

        self.__dialogue.text = ("Noughts" if self.__turn_manager.get_current_turn() == Placement.NOUGHT else "Crosses") + " turn."

        
    def create_button_callback(self, row: int, col: int):
        return lambda button: self.play_turn(button, row, col)
    
    def play_turn(self, button: Button, row: int, col: int):
        button.disabled = True

        turn: Placement = self.__turn_manager.get_current_turn()

        button.text = "O" if turn == Placement.NOUGHT else "X"

        self.__game.place(turn, row, col)

        if self.__game.game_is_over():
            for btn in self.__buttons:
                btn.disabled = True

            winner: Placement = self.__game.get_winner()

            if winner == Placement.NONE:
                self.__dialogue.text = "Its a draw!"

            self.__dialogue.text = ("Noughts" if winner == Placement.NOUGHT else "Crosses") + " Wins!"
            return

        self.__turn_manager.advance_turn()
        self.__dialogue.text = ("Noughts" if self.__turn_manager.get_current_turn() == Placement.NOUGHT else "Crosses") + " turn."

class NoughtsAndCrossesApp(App):
    def build(self):
        return GameView()

if __name__ == "__main__":
    app = NoughtsAndCrossesApp()
    app.run()