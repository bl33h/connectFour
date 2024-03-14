import numpy as np
from board import Board

class TemporalDifferenceAgent:
    def __init__(self, board: Board, piece: int, learning_rate=0.1, discount_factor=0.9):
        self.board = board
        self.piece = piece
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.values = {}

    def update_values(self, state: tuple, reward: int, next_state: tuple) -> None:
        """
        Update the state values using Temporal Difference
        """
        current_value = self.values.get(state, 0)
        next_value = self.values.get(next_state, 0)
        updated_value = current_value + self.learning_rate * (reward + self.discount_factor * next_value - current_value)
        self.values[state] = updated_value

    def get_best_move(self) -> int:
        """
        Get the best move using Temporal Difference
        """
        valid_locations = self.board.get_valid_locations()
        best_move = None
        best_value = -np.inf
        for col in valid_locations:
            row = self.board.get_next_open_row(col)
            if row is None:  # Check if column is full
                continue
            temp_board = self.board.copy()  # Create a temporary board to evaluate the move
            temp_board.drop_piece(row, col, self.piece)
            state = tuple(map(tuple, temp_board.state))  # Convert board state to hashable tuple
            value = self.values.get(state, 0)
            if value > best_value:
                best_value = value
                best_move = col
        return best_move
