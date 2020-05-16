import pygame
from pygame.sprite import Sprite
from settings import Settings


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.settings = Settings()
        self.screen = game.screen

        self.image = pygame.image.load("alien.bmp")
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)

        self.moving_up = True

    def update(self):
        if self.rect.y > 0 and self.moving_up is True:
            self.rect.y -= 1
        else:
            self.moving_up = False

        if self.rect.y < self.settings.screen_height \
                and self.moving_up is False:
            self.rect.y += 1

        else:
            self.moving_up = True
