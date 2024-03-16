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

    def get_state_for_tuples(self):
        # Place a 3 in the next open row of the column
        state = self.state.copy()
        for col in range(self.columns):
            if self.is_valid_location(col):
                row = self.get_next_open_row(col)
                state[row][col] = 3

        return state

    def get_tuples(self):
        n = 4
        board_state = self.get_state_for_tuples()
        rows, cols = len(board_state), len(board_state[0])
        tuples = []

        for i in range(rows):
            for j in range(cols):
                # Horizontal tuples
                if j + n <= cols:
                    tuples.append(tuple(board_state[i][j:j + n]))

                # Vertical tuples
                if i + n <= rows:
                    tuples.append(tuple(board_state[k][j] for k in range(i, i + n)))

                # Diagonal tuples (top-left to bottom-right)
                if i + n <= rows and j + n <= cols:
                    tuples.append(tuple(board_state[i + k][j + k] for k in range(n)))

                # Diagonal tuples (top-right to bottom-left)
                if i + n <= rows and j - n + 1 >= 0:
                    tuples.append(tuple(board_state[i + k][j - k] for k in range(n)))

        return tuples

    def vectorize(self):
        """
        Returns a list of integers representing the score of each tuple
        """
        tuples = self.get_tuples()
        vector = []
        for t in tuples:
            if len(t) == 4:
                vector.append(self.tuple_score(t))
        return vector

    def tuple_score(self, t):
        """
        Returns the score of a tuple
        :param t:
        :return:
        """
        # 3 → Empty and reachable
        # 0 → Empty and not reachable
        # 1 → Player 1 | Max
        # 2 → Player 2 | Min

        # 4 in a row
        if t.count(1) == 4:
            return 100
        elif t.count(2) == 4:
            return -100

        # 3 in a row and one empty and reachable
        elif t.count(1) == 3 and t.count(3) == 1:
            return 5
        elif t.count(2) == 3 and t.count(3) == 1:
            return -5

        # 2 in a row and two empty and reachable
        elif t.count(1) == 2 and t.count(3) == 2:
            return 2
        elif t.count(2) == 2 and t.count(3) == 2:
            return -2

        # In all other cases
        else:
            return 0
