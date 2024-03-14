from agents.minimax import MiniMax
from agents.temporal_difference import TemporalDifferenceAgent
from board import Board

class Connect4:
    """
    Connect4 game class
    Reference: https://www.youtube.com/watch?v=XpYz-q1lxu8
    """

    def __init__(self, board: Board = None, mode: str = 'pvai', use_alpha_beta: bool = False):
        self.board = board
        self.mode = mode

        self.agent1 = None
        self.agent2 = MiniMax(board=self.board, piece=2, use_alpha_beta=use_alpha_beta)
        if mode == 'aivai':
            self.agent1 = MiniMax(board=self.board, piece=1, use_alpha_beta=False)
        elif mode == 'pvai_td':
            self.agent2 = TemporalDifferenceAgent(board=self.board, piece=2)
        elif mode == 'mxvtd':
            self.agent1 = MiniMax(board=self.board, piece=1, use_alpha_beta=False)
            self.agent2 = TemporalDifferenceAgent(board=self.board, piece=2)
        elif mode == 'mxvtd-ab':
            self.agent1 = MiniMax(board=self.board, piece=1, use_alpha_beta=True)
            self.agent2 = TemporalDifferenceAgent(board=self.board, piece=2)

        self.is_game_over = False

        self.turn = 1  # 1 for player 1, 2 for player 2

    def drop_piece(self, col: int) -> None:
        """
        Handle click event
        """
        # If the column isn't full
        if self.board.is_valid_location(col):
            # Get where the piece will be dropped
            row = self.board.get_next_open_row(col)

            # Drop the piece
            self.board.drop_piece(row, col, self.turn)

            # Changes turns
            self.turn = (self.turn % 2) + 1

            # Check if the game is over
            self.is_game_over = self.board.is_game_over()
