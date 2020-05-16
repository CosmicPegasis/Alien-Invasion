#  Holds all the settings for the game
class Settings:
    def __init__(self):
        # Screen Settings
        self.screen_width = 720
        self.screen_height = 480
        self.screen_color = (250, 250, 250)

        # Ship settings
        self.ship_speed = 20

        # Bullet settings
        self.bullet_color = (250, 0, 0)
        self.bullet_width = 8
        self.bullet_height = 3
        self.bullet_speed = 40

        # Alien Settings
        self.alien_width = 30
        self.alien_height = 40
        self.alien_color = (0, 250, 0)
