import pygame
from settings import Settings


class Alien:
    def __init__(self, game):
        self.settings = Settings()
        self.width = self.settings.alien_width
        self.height = self.settings.alien_height

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.color = self.settings.alien_color

        self.rect = pygame.Rect(
            0, 0, self.width, self.height)

        self.rect.midleft = self.screen_rect.midleft
        self.moving = True

    def draw_alien(self):
        pygame.draw.rect(self.screen, self.color, self.rect)

    def update(self):
        if self.rect.top > self.screen_rect.top and self.moving is True:
            self.rect.y -= 1
        else:
            self.moving = False

        if self.rect.bottom < self.screen_rect.bottom and self.moving is False:
            self.rect.y += 1

        else:
            self.moving = True
