from src.board import Board


class Connect4:
    """
    Connect4 game class
    Reference: https://www.youtube.com/watch?v=XpYz-q1lxu8
    """

    def __init__(self):
        self.board = Board()
        self.game_over = False

        self.turn = 1  # 1 for player 1, 2 for player 2

    def play(self) -> None:
        self.board.reset()

        while not self.game_over:
            someone_won = False

            # Player 1's turn
            if self.turn == 1:
                col = int(input("Player 1: Column? (0-6): "))

                # If the column isn't full
                if self.board.is_valid_location(col):
                    # Get where the piece will be dropped
                    row = self.board.get_next_open_row(col)
                    # Drop the piece
                    someone_won = self.board.drop_piece(row, col, 1)

            # Player 2's turn
            else:
                col = int(input("Player 2: Column? (0-6): "))

                # If the column isn't full
                if self.board.is_valid_location(col):
                    # Get where the piece will be dropped
                    row = self.board.get_next_open_row(col)
                    # Drop the piece
                    someone_won = self.board.drop_piece(row, col, 2)

            # Print the board
            self.board.print()

            # Check if the game is over
            self.is_game_over(someone_won)

            # Changes turns
            self.turn = (self.turn % 2) + 1

    def is_game_over(self, did_winning_move: bool = False) -> None:
        """
        Check if the game is over
        """
        if did_winning_move:
            print(f"Player {self.turn} wins!")
            self.game_over = True
            return
