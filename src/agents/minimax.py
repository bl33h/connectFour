import numpy as np


class MiniMax:
    def __init__(self, use_alpha_beta=True):
        self.use_alpha_beta = use_alpha_beta
        self.max_depth = 4  # Profundidad máxima de búsqueda

    def set_alpha_beta(self, use_alpha_beta):
        self.use_alpha_beta = use_alpha_beta

    def minimax(self, state, depth, maximizing_player, alpha, beta):
        if depth == 0 or state.is_game_over():
            return 0

        valid_moves = [col for col in range(state.columns) if state.is_valid_location(col)]

        if maximizing_player:
            max_eval = float('-inf')
            for col in valid_moves:
                next_state = state.copy()
                row = next_state.get_next_open_row(col)
                next_state.drop_piece(row, col, 1)
                eval = self.minimax(next_state, depth - 1, False, alpha, beta)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if self.use_alpha_beta and beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = float('inf')
            for col in valid_moves:
                next_state = state.copy()
                row = next_state.get_next_open_row(col)
                next_state.drop_piece(row, col, 2)
                eval = self.minimax(next_state, depth - 1, True, alpha, beta)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if self.use_alpha_beta and beta <= alpha:
                    break
            return min_eval

    def get_best_move(self, state):
        # best_eval = float('-inf')
        # best_move = None
        # valid_moves = [col for col in range(state.columns) if state.is_valid_location(col)]
        #
        # for col in valid_moves:
        #     next_state = state.copy()
        #     row = next_state.get_next_open_row(col)
        #     next_state.drop_piece(row, col, 1)
        #     eval = self.minimax(next_state, self.max_depth, False, float('-inf'), float('inf'))
        #     if eval > best_eval:
        #         best_eval = eval
        #         best_move = col

        return np.random.choice([col for col in range(state.columns) if state.is_valid_location(col)])
