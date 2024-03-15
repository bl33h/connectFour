import numpy as np
import random
from board import Board

class TemporalDifferenceAgent:
    def __init__(self, board: Board, piece: int, learning_rate=0.5, discount_factor=0.9, epsilon=0.2, epsilon_decay=0.995):
        self.board = board
        self.piece = piece
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.epsilon_decay = epsilon_decay
        self.values = {}

    def update_values(self, state: tuple, reward: int, next_state: tuple) -> None:
        """
        Update the state values using Temporal Difference
        """
        current_value = self.values.get(state, 0)
        next_value = self.values.get(next_state, 0)
        updated_value = current_value + self.learning_rate * (reward + self.discount_factor * next_value - current_value)
        self.values[state] = updated_value

        if self.board.is_winning_move(self.piece):
            self.values[state] += 100
        elif self.board.is_winning_move(3 - self.piece):
            self.values[state] -= 100

    def heuristic_evaluation(self, temp_board, piece):
        """
        Evaluate the board using a heuristic
        """
        score = 0
        return score

    def get_best_move(self) -> int:
        """
        Get the best move using Temporal Difference
        """
        self.epsilon *= self.epsilon_decay
        valid_locations = self.board.get_valid_locations()

        if random.uniform(0, 1) < self.epsilon:
            return random.choice(valid_locations)

        best_move = None
        best_value = -np.inf

        for col in valid_locations:
            row = self.board.get_next_open_row(col)
            if row is None:
                continue
            
            # Block opponent's immediate winning move
            temp_board = self.board.copy()
            temp_board.drop_piece(row, col, 3 - self.piece)
            if temp_board.is_winning_move(3 - self.piece):
                return col  # Block the win
            
            # Evaluate move for the agent
            temp_board = self.board.copy()
            temp_board.drop_piece(row, col, self.piece)
            state = tuple(temp_board.state.flatten())
            base_value = self.values.get(state, 0)
            
            heuristic_value = self.heuristic_evaluation(temp_board, self.piece)
            value = base_value + heuristic_value + random.uniform(0, 0.01)

            if value > best_value:
                best_value = value
                best_move = col

        if best_move is None:
            return random.choice(valid_locations)
        return best_move
