import pygame
from settings import Settings


class Ship:
    def __init__(self, game):
        self.settings = Settings()

        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        self.ship = pygame.image.load('ship.bmp')
        self.rect = self.ship.get_rect()

        self.rect.midright = self.screen_rect.midright

        # Movement
        self.moving_up = False
        self.moving_down = False

    def blit_me(self):
        self.screen.blit(self.ship, self.rect)

    def move(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed
