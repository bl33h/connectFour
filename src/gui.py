import math

import pygame

from src.connect4 import Connect4


class GUI:
    def __init__(self, game: Connect4):
        self.square_size = 100  # Size of each square, pixels

        self.game = game
        self.rows = self.game.board.rows
        self.columns = self.game.board.columns

        self.width = self.columns * self.square_size
        self.height = (self.rows + 1) * self.square_size  # Add one row to show moving piece
        self.size = (self.width, self.height)

        self.screen = pygame.display.set_mode(self.size)

    def run(self) -> None:
        """
        Run the game
        """
        pygame.init()
        self.draw_board()
        while not self.game.is_game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEMOTION:
                    pass

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x_pos = event.pos[0]
                    col = int(math.floor(x_pos / self.square_size))
                    self.game.drop_piece(col)
                    self.draw_board()

    def draw_board(self) -> None:
        """
        Draw the board
        """
        board_state = self.game.board.get_state_flipped()
        for c in range(7):
            for r in range(6):
                pygame.draw.rect(
                    self.screen,
                    (0, 0, 255),
                    (c * self.square_size, r * self.square_size + self.square_size, self.square_size, self.square_size)
                )

                circle_color = (0, 0, 0)
                if board_state[r][c] == 1:
                    circle_color = (255, 0, 0)
                elif board_state[r][c] == 2:
                    circle_color = (255, 255, 0)
                pygame.draw.circle(
                    self.screen,
                    circle_color,
                    (
                        int(c * self.square_size + self.square_size / 2),
                        int(r * self.square_size + self.square_size + self.square_size / 2)
                    ),
                    int(self.square_size / 2 - 5)
                )

        pygame.display.update()

    def update_board(self, board: list) -> None:
        """
        Update the board
        """
        self.board_state = board
        self.draw_board()
