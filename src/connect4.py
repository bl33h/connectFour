from src.board import Board


class Connect4:
    """
    Connect4 game class
    Reference: https://www.youtube.com/watch?v=XpYz-q1lxu8
    """
    def __init__(self):
        self.board = Board()
        self.game_over = False

        self.turn = 0  # 0 for player 1, 1 for player 2

    def play(self):
        self.board.reset()

        while not self.game_over:
            # Player 1's turn
            if self.turn == 0:
                col = int(input("Player 1: Column? (0-6): "))

                # If the column isn't full
                if self.board.is_valid_location(col):
                    # Get where the piece will be dropped
                    row = self.board.get_next_open_row(col)
                    # Drop the piece
                    self.board.drop_piece(row, col, 1)

            # Player 2's turn
            else:
                col = int(input("Player 2: Column? (0-6): "))

                # If the column isn't full
                if self.board.is_valid_location(col):
                    # Get where the piece will be dropped
                    row = self.board.get_next_open_row(col)
                    # Drop the piece
                    self.board.drop_piece(row, col, 2)

            # Print the board
            self.board.print()

            # Changes turns
            self.turn = (self.turn + 1) % 2
