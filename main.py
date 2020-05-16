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
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # Inits the ship
        self.ship = Ship(self)
        # Sets the program running state to true
        self.program_running = True
        # Defines a new group for bullet sprites
        self.bullets = pygame.sprite.Group()

        # Inits an alien
        self.aliens = pygame.sprite.Group()

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

        if event.key == pygame.K_q:
            self.program_running = False

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
        self.ship.blit_me()
        self.create_fleet()
        self.aliens.draw(self.screen)
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
            for alien in self.aliens:
                col_de = CollisionDetection(self, bullet, alien)
                col_de.detect(game)

    def create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_width = self.ship.rect.width

        available_space_x = self.settings.screen_width - alien_height - \
            ship_width
        num_aliens = available_space_x // (alien_width * 2)

        available_space_y = self.settings.screen_height - alien_height * 2
        num_rows = available_space_y // (alien_height)

        for row_number in range(num_rows):
            for alien_number in range(num_aliens):
                self.create_alien(alien_number, row_number)

    def create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        alien.y = alien_height + (2 * alien_height * row_number)
        alien.x = alien_width + (2 * alien_width * alien_number)

        alien.rect.x = alien.x
        alien.rect.y = alien.y

        self.aliens.add(alien)
    # Main

    def run_game(self):
        while self.program_running:
            self.check_events()
            self.bullets.update()
            self.update_screen()
            self.ship_update()
            self.aliens.update()
            self.col_de()


# Runs the game
game = Game()
game.run_game()

pygame.quit()
