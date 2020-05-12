import pygame
from pygame.sprite import Sprite

# class for Bullet


class Bullet(Sprite):
    # Inherits from Sprite class
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.bullet_color = (250, 0, 0)

        # Defines a rectangle for bullet
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        # Aligns the bullet with ship
        self.rect.midright = game.ship.rect.midright
        self.x = float(self.rect.x)

    # Updates the position of the bullet
    def update(self):
        self.x -= self.settings.bullet_speed
        self.rect.x = self.x

    # Draws the defined rectangle from scratch
    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.bullet_color, self.rect)
