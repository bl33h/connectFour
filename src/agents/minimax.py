import numpy as np

from src.board import Board

MAX_DEPTH = 4  # The maximum depth the MiniMax algorithm will reach
WINNING_SCORE = 1_000_000
LOSING_SCORE = -1_000_000
TIE_SCORE = 0

SCORE_BLOCK_OPPONENT_WINNING_MOVE = -1_000
SCORE_IN_A_ROW = {
    4: WINNING_SCORE,
    3: 5,
    2: 2,
    1: 1,
}


class MiniMax:
    def __init__(self, board: Board, piece: int, use_alpha_beta=True):
        self.board = board
        self.piece = piece  # The int that represents the agent's piece
        self.opp_piece = piece % 2 + 1  # The int that represents the opponent's piece
        self.use_alpha_beta = use_alpha_beta

    def minimax(self, board: Board, depth: int, alpha: float, beta: float, maximizing_player: bool) -> tuple:
        valid_locations = board.get_valid_locations()
        is_terminal = board.is_game_over()
        if depth == 0 or is_terminal:
            if is_terminal:
                if board.is_winning_move(self.piece):
                    return None, WINNING_SCORE
                elif board.is_winning_move(self.opp_piece):
                    return None, LOSING_SCORE
                else:
                    return None, TIE_SCORE
            else:  # Depth is 0
                return None, self.score_position(board.state, self.piece)

        if maximizing_player:
            score = -np.inf
            best_column = None
            for col in valid_locations:
                row = board.get_next_open_row(col)
                temp_board = board.copy()
                temp_board.drop_piece(row, col, self.piece)
                _, new_score = self.minimax(temp_board, depth - 1, alpha, beta, False)
                if new_score > score:  # This column (col) is the best so far
                    score = new_score
                    best_column = col
                alpha = max(alpha, score)
                if self.use_alpha_beta and beta <= alpha:
                    break
            return best_column, score

        else:
            score = np.inf
            best_column = None
            for col in valid_locations:
                row = board.get_next_open_row(col)
                temp_board = board.copy()
                temp_board.drop_piece(row, col, self.opp_piece)
                _, new_score = self.minimax(temp_board, depth - 1, alpha, beta, True)
                if new_score < score:
                    score = new_score
                    best_column = col
                beta = min(beta, score)
                if self.use_alpha_beta and beta <= alpha:
                    break
            return best_column, score

    def score_position(self, board: np.ndarray, piece: int) -> int:
        """
        Evaluar el tablero
        """
        score = 0
        # Each 'window' is a section of 4 adjacent locations in the board

        # Score Center Column → Center column is the best to play
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

        if window.count(self.piece) == 4:  # Winning move
            score += WINNING_SCORE
        elif window.count(self.piece) == 3 and window.count(0) == 1:  # 3 in a row
            score += SCORE_IN_A_ROW[3]
        elif window.count(self.piece) == 2 and window.count(0) == 2:  # 2 in a row
            score += SCORE_IN_A_ROW[2]

        if window.count(self.opp_piece) == 3 and window.count(0) == 1:  # Block opponent's 3 in a row
            score -= SCORE_BLOCK_OPPONENT_WINNING_MOVE

        return score

    def get_best_move(self) -> int:
        """
        Get the best move with the MiniMax algorithm
        """
        best_col, _ = self.minimax(self.board, MAX_DEPTH, -np.inf, np.inf, True)
        return best_col
