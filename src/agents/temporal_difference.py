import random

import numpy as np

from src.board import Board


class TemporalDifferenceAgent:
    def __init__(self, board: Board, piece: int, learning_rate=0.5, discount_factor=0.9, epsilon=0.2,
                 epsilon_decay=0.995):
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
        updated_value = current_value + self.learning_rate * (
                reward + self.discount_factor * next_value - current_value)
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
        vector = self.board.vectorize()
        print(vector)
        return self.board.get_valid_locations()[0]
