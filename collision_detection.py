# Used for collision detection
class CollisionDetection:
    # Brings in the rects froom game and bullet
    def __init__(self, game, bullet, alien):
        # Alien
        self.x1 = alien.rect.x
        self.y1 = alien.rect.y
        self.h1 = alien.rect.height
        self.w1 = alien.rect.width

        # Bullet
        self.x2 = bullet.rect.x
        self.y2 = bullet.rect.y
        self.h2 = game.settings.bullet_height
        self.w2 = game.settings.bullet_width

    # Collision Detection Logic
    def detect(self, alien):
        if self.x2 > self.x1 and self.x2 < self.x1 + self.w1 and \
                self.y2 > self.y1 and self.y2 < self.y1 + self.h1:

            alien.kill()
