from src.board import Board
from src.connect4 import Connect4
from src.gui import GUI


class Game:
    def __init__(self, mode: str, pruning: bool):
        self.rows = 6
        self.columns = 7
        self.board = Board(rows=self.rows, columns=self.columns)
        self.connect4 = Connect4(self.board)
        self.gui = GUI(game=self.connect4)

        self.is_active = True

    def play(self):
        self.connect4.board.reset()
        self.gui.run()
        self.is_active = False
