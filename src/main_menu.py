import sys
import pygame
from game import Game

class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 48)
        self.button_font = pygame.font.Font(None, 36)
        self.title = self.font.render("Game Menu", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=(400, 80))
        self.pvai_button = pygame.Rect(300, 200, 200, 50)
        self.aivai_button = pygame.Rect(300, 300, 200, 50)
        button_width = 305
        screen_width = 800
        self.alpha_beta_toggle = pygame.Rect((screen_width - button_width) / 2, 400, button_width, 50)
        self.alpha_beta_enabled = True

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.pvai_button.collidepoint(event.pos):
                game = Game('pvai', self.alpha_beta_enabled)
                game.play()
                if not game.is_active:  # check if the game is still active
                    return False  # return False to indicate that the game has ended

            elif self.aivai_button.collidepoint(event.pos):
                game = Game('aivai', self.alpha_beta_enabled)
                game.play()
                if not game.is_active:  # check if the game is still active
                    return False  # return False to indicate that the game has ended

            elif self.alpha_beta_toggle.collidepoint(event.pos):
                self.alpha_beta_enabled = not self.alpha_beta_enabled

        return True  # return True to indicate that the game is still active

    def draw_text(self, text, rect, font):
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(
            center=rect.center)  # get the rectangle of the text surface and set its center to the center of the button
        self.screen.blit(text_surface, text_rect)  # blit the text surface at the center of the button

    def draw_button(self, rect, text, font):
        pygame.draw.rect(self.screen, (24, 138, 225), rect)
        self.draw_text(text, rect, font)

    def draw(self):
        self.screen.fill((18, 46, 67))
        self.screen.blit(self.title, self.title_rect)
        self.draw_button(self.pvai_button, "PvAI", self.button_font)
        self.draw_button(self.aivai_button, "AIvAI", self.button_font)
        self.draw_button(self.alpha_beta_toggle, "Alpha-Beta Pruning: " + ("ON" if self.alpha_beta_enabled else "OFF"),
                         self.button_font)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if not self.handle_event(event):  # check if the game is still active
                    return  # return from the run method if the game has ended

            self.draw()
            pygame.display.flip()


if __name__ == "__main__":
    MainMenu().run()