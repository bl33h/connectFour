import numpy as np

from src.board import Board


class MiniMax:
    def __init__(self, board: Board, piece: int, use_alpha_beta=True):
        self.board = board
        self.piece = piece  # The int that represents the agent's piece
        self.use_alpha_beta = use_alpha_beta
        self.max_depth = 4  # Profundidad máxima de búsqueda

    def score_position(self, board: np.ndarray, piece: int) -> int:
        """
        Evaluar el tablero
        """
        score = 0
        # Each 'window' is a section of 4 adjacent locations in the board

        # Score Center Column
        center_array = [int(i) for i in list(board[:, self.board.columns // 2])]
        center_count = center_array.count(piece)
        score += center_count * 3

        # Score Horizontal
        for r in range(board.shape[0]):
            row_array = [int(i) for i in list(board[r, :])]
            for c in range(board.shape[1] - 3):
                window = row_array[c:c + 4]
                score += self.evaluate_window(window)

        # Score Vertical
        for c in range(board.shape[1]):
            col_array = [int(i) for i in list(board[:, c])]
            for r in range(board.shape[0] - 3):
                window = col_array[r:r + 4]
                score += self.evaluate_window(window)

        # Score positive sloped diagonal
        for r in range(board.shape[0] - 3):
            for c in range(board.shape[1] - 3):
                window = [board[r + i][c + i] for i in range(4)]
                score += self.evaluate_window(window)

        # Score negative sloped diagonal
        for r in range(board.shape[0] - 3):
            for c in range(board.shape[1] - 3):
                window = [board[r + 3 - i][c + i] for i in range(4)]
                score += self.evaluate_window(window)

        return score

    def evaluate_window(self, window: list) -> int:
        """
        Evaluar la ventana
        """
        score = 0
        opponent_piece = self.piece % 2 + 1

        if window.count(self.piece) == 4:  # Winning move
            score += 1_000
        elif window.count(self.piece) == 3 and window.count(0) == 1:  # 3 in a row
            score += 5
        elif window.count(self.piece) == 2 and window.count(0) == 2:  # 2 in a row
            score += 2

        if window.count(opponent_piece) == 3 and window.count(0) == 1:  # Block opponent's 3 in a row
            score -= 100

        return score

    def get_best_move(self) -> int:
        """
        Obtener el mejor movimiento
        """
        valid_locations = self.board.get_valid_locations()

        best_score = 0
        best_col = np.random.choice(valid_locations)

        for col in valid_locations:
            row = self.board.get_next_open_row(col)
            temp_board = self.board.copy()
            temp_board.drop_piece(row, col, self.piece)
            score = self.score_position(temp_board.state, self.piece)
            if score > best_score:
                best_score = score
                best_col = col

        return best_col
