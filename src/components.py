import numpy as np

class gameComponents:
    def __init__(self):
        self.board = np.zeros((6, 7))
        self.gameOver = False
        self.turn = 0
        self.rows = 6

    def piecesDrop(self, row, column, piece):
        self.board[row][column] = piece

    def validSpot(self, column):
        if column < 0 or column >= len(self.board[0]):
            return False
        return self.board[self.rows - 1][column] == 0

    def openRow(self, column):
        for r in range(self.rows):
            if self.board[r][column] == 0:
                return r

    def playTurn(self):
        try:
            print("\n")
            print(self.board)
            column = int(input(f"player {self.turn + 1} selection (0-6): "))
            if self.validSpot(column):
                row = self.openRow(column)
                self.piecesDrop(row, column, self.turn + 1)
                self.turn = (self.turn + 1) % 2
            else:
                print("invalid spot, try again.")
        except ValueError:
            print("invalid input, enter a number.")

    def startGame(self):
        while not self.gameOver:
            self.playTurn()