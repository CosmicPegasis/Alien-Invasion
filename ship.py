import pygame
from settings import Settings

# Ship class


class Ship:
    def __init__(self, game):
        # Inits a setting instance
        self.settings = Settings()

        # Imports scree attributess from main
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()

        # Loads ship images and
        self.ship = pygame.image.load('ship.bmp')
        # Gets the rect and then assign it to a var
        self.rect = self.ship.get_rect()

        # Aligns the ship to the mid right of the screen
        self.rect.midright = self.screen_rect.midright

        # Movement Flags
        self.moving_up = False
        self.moving_down = False

    # Draws the ship to screen
    def blit_me(self):
        self.screen.blit(self.ship, self.rect)

    # Movement logic
    def move(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.rect.y -= self.settings.ship_speed

        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed
