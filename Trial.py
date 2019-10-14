import time
from functions import *
from our_classes import *

pygame.init()

windows_width = 1000
windows_height = 500

win = pygame.display.set_mode((windows_width, windows_height))
pygame.display.set_caption("First Game")



#main loop
player1 = player(700, 400, 40, 60, 5, (255, 0, 0), 10)
computer = player(100, 400, 40, 60, 5, (0, 255, 0), 10)

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
            computer.life -= 1
            if computer.life == 0:
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
