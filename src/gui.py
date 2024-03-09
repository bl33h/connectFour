import pygame


class GUI:
    def __init__(self, rows: int = 6, columns: int = 7):
        self.square_size = 100  # Size of each square, pixels
        self.width = columns * self.square_size
        self.height = (rows + 1) * self.square_size  # Add one row to show moving piece
        self.size = (self.width, self.height)

        self.screen = pygame.display.set_mode(self.size)

    def run(self) -> None:
        """
        Run the game
        """
        pygame.init()

        self.draw_board()

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEMOTION:
                    pass

                if event.type == pygame.MOUSEBUTTONDOWN:
                    pass

    def draw_board(self) -> None:
        """
        Draw the board
        """
        for c in range(7):
            for r in range(6):
                pygame.draw.rect(
                    self.screen,
                    (0, 0, 255),
                    (c * self.square_size, r * self.square_size + self.square_size, self.square_size, self.square_size)
                )

                pygame.draw.circle(
                    self.screen,
                    (0, 0, 0),
                    (int(c * self.square_size + self.square_size / 2),
                     int(r * self.square_size + self.square_size + self.square_size / 2)),
                    45
                )

        pygame.display.update()
