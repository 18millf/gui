from enum import Enum, IntFlag

class Placement(Enum):
    NONE = 0
    CROSS = 1
    NOUGHT = 2

class Grid(IntFlag):
    M11 = 1
    M12 = 2
    M13 = 4
    M21 = 8
    M22 = 16
    M23 = 32
    M31 = 64
    M32 = 128
    M33 = 256

class Game:
    __WINNING_POSITIONS = [Grid(7), Grid(56), Grid(196), Grid(73), Grid(146), Grid(292), Grid(273), Grid(84)]
    __GRID_REFERENCE: list(list(Grid)) = [
        [Grid.M11, Grid.M12, Grid.M13],
        [Grid.M21, Grid.M22, Grid.M23],
        [Grid.M31, Grid.M32, Grid.M33]
    ]

    def __init__(self) -> None:
        self.__turn = 0
        self.__grid = [[Placement.NONE for _ in range(3)] for _ in range(3)]
        self.__player_grids: dict(Placement, Grid) = { Placement.CROSS: Grid(0), Placement.NOUGHT: Grid(0) }
    
    def place(self, placement: Placement, row: int, col: int) -> bool:
        assert row >= 0 and row < 3
        assert col >= 0 and col < 3

        self.__grid[row][col] = placement

        # bitwise OR to insert bitflag for the position played
        self.__player_grids[placement] |= self.__player_grids[placement] | self.__coords_to_gridspace(row, col)

        self.__turn += 1

        return self.game_is_over()

    def __coords_to_gridspace(self, row: int, col: int) -> Grid:
        return Game.__GRID_REFERENCE[row][col]

    def game_is_over(self) -> bool:
        if self.__turn >= 9: # cant play more than 9 turns, 3x3 grid (grid is filled, conditions for a draw)
            return True
        
        if self.__turn < 5: # cant win in less than 5 turns
            return False

        return self.get_winner() != Placement.NONE # someone won

    def get_winner(self) -> Placement:
        winner: Placement = Placement.NONE # default

        # check if any of the players have got a winning pattern by checking the bit flags
        for pos in Game.__WINNING_POSITIONS:
            if pos & self.__player_grids[Placement.NOUGHT] == pos:
                winner = Placement.NOUGHT
                break
            if pos & self.__player_grids[Placement.CROSS] == pos:
                winner = Placement.CROSS
                break

        return winner