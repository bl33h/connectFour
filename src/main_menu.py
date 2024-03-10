import sys

import pygame

from src.game import Game


class MainMenu:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.font = pygame.font.Font(None, 48)
        self.button_font = pygame.font.Font(None, 36)
        self.title = self.font.render("Game Menu", True, (255, 255, 255))
        self.title_rect = self.title.get_rect(center=(400, 80))
        self.pvp_button = pygame.Rect(300, 200, 200, 50)
        self.pvai_button = pygame.Rect(300, 300, 200, 50)
        self.alpha_beta_toggle = pygame.Rect(300, 400, 200, 50)
        self.alpha_beta_enabled = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.pvp_button.collidepoint(event.pos):
                Game(
                    'pvp',
                    self.alpha_beta_enabled
                ).play()

            elif self.pvai_button.collidepoint(event.pos):
                Game(
                    'pvai',
                    self.alpha_beta_enabled
                ).play()
            elif self.alpha_beta_toggle.collidepoint(event.pos):
                self.alpha_beta_enabled = not self.alpha_beta_enabled

    def draw_text(self, text, rect, font):
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect(
            center=rect.center)  # get the rectangle of the text surface and set its center to the center of the button
        self.screen.blit(text_surface, text_rect)  # blit the text surface at the center of the button

    def draw_button(self, rect, text, font):
        pygame.draw.rect(self.screen, (0, 0, 255), rect)
        self.draw_text(text, rect, font)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.title, self.title_rect)
        self.draw_button(self.pvp_button, "PvP", self.button_font)
        self.draw_button(self.pvai_button, "PvAI", self.button_font)
        self.draw_button(self.alpha_beta_toggle, "Alpha-Beta Pruning: " + ("ON" if self.alpha_beta_enabled else "OFF"),
                         self.button_font)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.handle_event(event)

            self.draw()
            pygame.display.flip()


if __name__ == "__main__":
    MainMenu().run()
