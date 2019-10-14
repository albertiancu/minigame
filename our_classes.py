
class player(object):
    def __init__(self, x, y, width, height, vel, color, life):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.isJump = False
        self.jumpCount = 10
        self.dead = False
        self.color = color
        self.life = life

    def draw(self, win):
        if not self.dead:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))



