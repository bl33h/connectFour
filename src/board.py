import numpy as np


class Board:
    def __init__(self, rows: int = 6, columns: int = 7, state: np.ndarray = None):
        self.rows = rows
        self.columns = columns
        self.state = np.zeros((rows, columns)) if state is None else state

    def reset(self) -> None:
        self.state = np.zeros((self.rows, self.columns))

    def drop_piece(self, row: int, col: int, piece: int) -> None:
        self.state[row][col] = piece

    def is_game_over(self) -> bool:
        return self.is_full() or self.is_winning_move(1) or self.is_winning_move(2)

    def is_full(self) -> bool:
        return 0 not in self.state[self.rows - 1]

    def is_winning_move(self, piece: int) -> bool:
        # Check horizontal locations for win
        for c in range(self.columns - 3):
            for r in range(self.rows):
                if self.state[r][c] == piece and self.state[r][c + 1] == piece and self.state[r][c + 2] == piece and \
                        self.state[r][c + 3] == piece:
                    return True

        # Check vertical locations for win
        for c in range(self.columns):
            for r in range(self.rows - 3):
                if self.state[r][c] == piece and self.state[r + 1][c] == piece and self.state[r + 2][c] == piece and \
                        self.state[r + 3][c] == piece:
                    return True

        # Check positively sloped diagonals
        for c in range(self.columns - 3):
            for r in range(self.rows - 3):
                if self.state[r][c] == piece and self.state[r + 1][c + 1] == piece and self.state[r + 2][
                    c + 2] == piece and \
                        self.state[r + 3][c + 3] == piece:
                    return True

        # Check negatively sloped diagonals
        for c in range(self.columns - 3):
            for r in range(3, self.rows):
                if self.state[r][c] == piece and self.state[r - 1][c + 1] == piece and self.state[r - 2][
                    c + 2] == piece and \
                        self.state[r - 3][c + 3] == piece:
                    return True

        # It isn't a winning move
        else:
            return False

    def is_valid_location(self, column: int) -> bool:
        """
        Check if the column is not full
        """
        # If the columns is full, the top row will not be 0
        return np.all(self.state[self.rows - 1][column] == 0)

    def get_valid_locations(self) -> list:
        """
        Get the valid locations where a piece can be dropped
        """
        valid_locations = []
        for col in range(self.columns):
            if self.is_valid_location(col):
                valid_locations.append(col)
        return valid_locations

    def get_next_open_row(self, column: int) -> int:
        """
        Get the next open row in the column
        """
        for row in range(self.rows):
            if self.state[row][column] == 0:
                return row

    def print(self):
        print(np.flip(self.state, 0))

    def get_state(self):
        return self.state

    def get_state_flipped(self):
        return np.flip(self.state, 0)

    def copy(self) -> 'Board':
        return Board(
            rows=self.rows,
            columns=self.columns,
            state=self.state.copy()
        )
