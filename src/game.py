from src.board import Board
from src.connect4 import Connect4
from src.gui import GUI


class Game:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.board = Board(rows=self.rows, columns=self.columns)
        self.connect4 = Connect4(self.board)
        self.gui = GUI(game=self.connect4)

    def play(self):
        self.connect4.board.reset()
        self.gui.run()
