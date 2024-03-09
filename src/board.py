import numpy as np


class Board:
    def __init__(self, rows=6, columns=7):
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((rows, columns))

    def reset(self):
        self.board = np.zeros((self.rows, self.columns))

    def drop_piece(self, row, col, piece):
        self.board[row][col] = piece

    def is_valid_location(self, column):
        """
        Check if the column is not full
        """
        # If the columns is full, the top row will not be 0
        return self.board[self.rows - 1][column] == 0

    def get_next_open_row(self, column):
        """
        Get the next open row in the column
        """
        for row in range(self.rows):
            if self.board[row][column] == 0:
                return row

    def print(self):
        print(np.flip(self.board, 0))

