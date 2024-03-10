import math

import pygame

from src.connect4 import Connect4


class GUI:
    def __init__(self, game: Connect4):
        pygame.init()
        pygame.font.init()

        self.square_size = 75  # Size of each square, pixels

        self.game = game
        self.rows = self.game.board.rows
        self.columns = self.game.board.columns

        self.width = self.columns * self.square_size
        self.height = (self.rows + 1) * self.square_size  # Add one row to show moving piece
        self.size = (self.width, self.height)

        self.screen = pygame.display.set_mode(self.size)

        self.font = pygame.font.SysFont('monospace', 50)

    def run(self) -> None:
        """
        Run the game
        """
        self.draw_board()
        if self.game.mode == 'pvai':
            while not self.game.is_game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                    if event.type == pygame.MOUSEMOTION:
                        x_pos = event.pos[0]
                        self.show_piece_to_drop(x_pos)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        x_pos = event.pos[0]
                        col = int(math.floor(x_pos / self.square_size))
                        self.game.drop_piece(col)
                        self.draw_board()

                        # Automatically make the AI move
                        if not self.game.is_game_over:
                            col = self.game.agent2.get_best_move()
                            self.game.drop_piece(col)
                            self.draw_board()
        else:  # AI vs AI
            while not self.game.is_game_over:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                if self.game.turn == 1:
                    col = self.game.agent1.get_best_move()
                    self.game.drop_piece(col)
                    self.draw_board()
                else:
                    col = self.game.agent2.get_best_move()
                    self.game.drop_piece(col)
                    self.draw_board()

        # Game over
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.width, self.square_size))
        self.game.turn = (self.game.turn % 2) + 1  # Change turn to the winner
        label = self.font.render(
            f"Player {self.game.turn} wins!",
            1,
            (255, 0, 0) if self.game.turn == 1 else (255, 255, 0)
        )
        self.screen.blit(label, (40, 10))
        pygame.display.update()
        pygame.time.wait(3000)

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

    def show_piece_to_drop(self, x_pos) -> None:
        """
        Show the piece to drop
        """
        pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, self.width, self.square_size))
        pygame.draw.circle(
            self.screen,
            (255, 0, 0),
            (x_pos, int(self.square_size / 2)),
            int(self.square_size / 2 - 5)
        )
        pygame.display.update()
