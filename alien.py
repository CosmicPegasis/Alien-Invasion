import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

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

        if self.rect.bottom < self.screen_rect.bottom \
                and self.moving_up is False:
            self.rect.y += 1

        else:
            self.moving_up = True
