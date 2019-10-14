import pygame
import datetime
import time

pygame.init()

windows_width = 100
windows_height = 500

win = pygame.display.set_mode((windows_width, windows_height))
pygame.display.set_caption("First Game")


class player(object):
    def __init__(self, x, y, width, height, vel, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        self.isJump = False
        self.jumpCount = 10
        self.dead = False
        self.color = color

    def draw(self, win):
        if not self.dead:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))




def drawWindow():
    win.fill((0, 0, 0))  # Fills the screen with black
    player1.draw(win)
    computer.draw(win)
    for i in shots:
        pygame.draw.rect(win, (0, 0, 255), (i[0], i[1], 10, 10))
    pygame.display.update()


#main loop
player1 = player(700, 400, 40, 60, 5, (255, 0, 0))
computer = player(100, 400, 40, 60, 5, (0, 255, 0))

run = True
shots = []
lastShotTime = time.time()

while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and (player1.x > player1.vel):
        player1.x -= player1.vel

    if keys[pygame.K_RIGHT] and (player1.x + player1.width + player1.vel < windows_width):
        player1.x += player1.vel

    if keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]:
        if time.time() - lastShotTime >= 0.2:
            shots.append((player1.x, player1.y))
            lastShotTime = time.time()

    newShots = []
    for i in shots:
        i = (i[0] - 100, i[1])
        if i[0] < 0:
            continue
        if i[0] <= computer.x + computer.width and (i[1] < computer.y + computer.height and i[1] + 5 > computer.y) and not computer.dead:
            computer.dead = True
            continue

        newShots.append(i)

    shots = newShots

    if not player1.isJump:
        # if keys[pygame.K_UP] and (y1 > vel):
        #     y1 -= vel
        #
        # if keys[pygame.K_DOWN] and (y1 + height + vel < windows_height):
        #     y1 += vel

        if keys[pygame.K_SPACE]:
            player1.isJump = True


    else:
        if player1.jumpCount >= -10:
            neg = 1
            if player1.jumpCount < 0:
                neg = -1
            player1.y -= (player1.jumpCount ** 2) * 0.5 * neg
            player1.jumpCount -= 1

        else:
            player1.isJump = False
            player1.jumpCount = 10


    drawWindow()



pygame.quit()
