import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from collision_detection import CollisionDetection


# Main class
class Game:
    def __init__(self):
        # Inits the Settings class
        self.settings = Settings()
        # Makes a display
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Inits the ship
        self.ship = Ship(self)
        # Sets the program running state to true
        self.program_running = True
        # Defines a new group for bullet sprites
        self.bullets = pygame.sprite.Group()

        # Inits an alien
        self.alien = Alien(self)

    # Checks for keyboard presses

    def check_events(self):
        for event in pygame.event.get():
            # Checks if user pressed the cross button
            if event.type == pygame.QUIT:
                self.program_running = False

            # Checks if user pressed a key
            if event.type == pygame.KEYDOWN:
                self.keydown_events(event)
            # Checks if user released a key
            if event.type == pygame.KEYUP:
                self.keyup_events(event)

    # All registerd events that can happen when key is pressed
    def keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = True

        if event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        if event.key == pygame.K_SPACE:
            self.fire_bullet()

    # All registered events when a key is released

    def keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.ship.moving_up = False

        if event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    # Updates the screen i.e fills color etc
    def update_screen(self):
        self.screen.fill(self.settings.screen_color)
        self.update_bullets()
        self.alien.draw_alien()
        self.ship.blit_me()
        pygame.display.flip()

    # Fires a bullet if less than three bullets are on the screen
    def fire_bullet(self):
        if len(self.bullets) < 3:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    # Creates new bullets and removes out of screen bullets
    def update_bullets(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        # Prevents memory leak by deleting bullets which are off screen
        for bullet in self.bullets.copy():
            if bullet.rect.x < 0:
                self.bullets.remove(bullet)

    # Update ship position
    def ship_update(self):
        self.ship.move()

    # Collision Detection
    def col_de(self):
        for bullet in self.bullets.copy():
            col_de = CollisionDetection(self, bullet)
            col_de.detect(game)

    # Main
    def run_game(self):
        while self.program_running:
            self.check_events()
            self.bullets.update()
            self.update_screen()
            self.ship_update()
            self.alien.update()
            self.col_de()


# Runs the game
game = Game()
game.run_game()

pygame.quit()
