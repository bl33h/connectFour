import numpy as np


class Board:
    def __init__(self, rows: int = 6, columns: int = 7):
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((rows, columns))

    def reset(self) -> None:
        self.board = np.zeros((self.rows, self.columns))

    def drop_piece(self, row: int, col: int, piece: int) -> bool:
        self.board[row][col] = piece

        return self._is_winning_move(row, col, piece)

    def _is_winning_move(self, row: int, col: int, piece: int) -> bool:
        # Check north of where the piece was dropped
        if (
                row < self.rows - 3 and  # Make sure we don't go out of bounds
                self.board[row + 1][col] == piece and  # Check the pieces above
                self.board[row + 2][col] == piece and
                self.board[row + 3][col] == piece
        ):
            return True

        # Check north-east of where the piece was dropped
        elif (
                row < self.rows - 3 and  # Make sure we don't go out of bounds
                col < self.columns - 3 and  # Make sure we don't go out of bounds
                self.board[row + 1][col + 1] == piece and  # Check the pieces above
                self.board[row + 2][col + 2] == piece and
                self.board[row + 3][col + 3] == piece
        ):
            return True

        # Check east of where the piece was dropped
        elif (
                col < self.columns - 3 and  # Make sure we don't go out of bounds
                self.board[row][col + 1] == piece and  # Check the pieces to the right
                self.board[row][col + 2] == piece and
                self.board[row][col + 3] == piece
        ):
            return True

        # Check south-east of where the piece was dropped
        elif (
                row > 2 and  # Make sure we don't go out of bounds
                col < self.columns - 3 and  # Make sure we don't go out of bounds
                self.board[row - 1][col + 1] == piece and  # Check the pieces below
                self.board[row - 2][col + 2] == piece and
                self.board[row - 3][col + 3] == piece
        ):
            return True

        # Check south of where the piece was dropped
        elif (
                row > 2 and  # Make sure we don't go out of bounds
                self.board[row - 1][col] == piece and  # Check the pieces below
                self.board[row - 2][col] == piece and
                self.board[row - 3][col] == piece
        ):
            return True

        # Check south-west of where the piece was dropped
        elif (
                row > 2 and  # Make sure we don't go out of bounds
                col > 2 and  # Make sure we don't go out of bounds
                self.board[row - 1][col - 1] == piece and  # Check the pieces below
                self.board[row - 2][col - 2] == piece and
                self.board[row - 3][col - 3] == piece
        ):
            return True

        # Check west of where the piece was dropped
        elif (
                col > 2 and  # Make sure we don't go out of bounds
                self.board[row][col - 1] == piece and  # Check the pieces to the left
                self.board[row][col - 2] == piece and
                self.board[row][col - 3] == piece
        ):
            return True

        # Check north-west of where the piece was dropped
        elif (
                row < self.rows - 3 and  # Make sure we don't go out of bounds
                col > 2 and  # Make sure we don't go out of bounds
                self.board[row + 1][col - 1] == piece and  # Check the pieces above
                self.board[row + 2][col - 2] == piece and
                self.board[row + 3][col - 3] == piece
        ):
            return True

        # It isn't a winning move
        else:
            return False

    def is_valid_location(self, column: int) -> bool:
        """
        Check if the column is not full
        """
        # If the columns is full, the top row will not be 0
        return self.board[self.rows - 1][column] == 0

    def get_next_open_row(self, column: int) -> int:
        """
        Get the next open row in the column
        """
        for row in range(self.rows):
            if self.board[row][column] == 0:
                return row

    def print(self):
        print(np.flip(self.board, 0))
