# Used for collision detection
class CollisionDetection:
    # Brings in the rects froom game and bullet
    def __init__(self, game, bullet):
        # Alien
        self.x1 = game.alien.rect.x
        self.y1 = game.alien.rect.y
        self.h1 = game.alien.height
        self.w1 = game.alien.width

        # Bullet
        self.x2 = bullet.rect.x
        self.y2 = bullet.rect.y
        self.h2 = game.settings.bullet_height
        self.w2 = game.settings.bullet_width

    # Collision Detection Logic
    def detect(self, game):
        if self.x2 > self.x1 and self.x2 < self.x1 + self.w1 and \
                self.y2 > self.y1 and self.y2 < self.y1 + self.h1:
            game.program_running = False
            print('You won!')
