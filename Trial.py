import time
import pygame
from functions import *
from our_classes import *

#init
pygame.init()
windows_width = 1000
windows_height = 500
win = pygame.display.set_mode((windows_width, windows_height))
pygame.display.set_caption("First Game")
player1 = Player(700, 400, 40, 60, 5, (255, 0, 0), 10)
player2 = Player(100, 400, 40, 60, 5, (0, 255, 0), 10)
shots1 = Shots()
shots2 = Shots()
game = Game(win, player1, player2, shots1, shots2)

run = True


while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and (game.player1.x > game.player1.vel):
        game.player1.x -= game.player1.vel

    if keys[pygame.K_RIGHT] and (game.player1.x + game.player1.width + game.player1.vel < windows_width):
        game.player1.x += game.player1.vel

    if keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]:
        if time.time() - game.shots1.lastShotTime >= 0.2:
            game.shots1.addShot((game.player1.x, game.player1.y))
            game.shots1.lastShotTime = time.time()

    newShots = []
    for i in game.shots1.shotsList:
        i = (i[0] - 100, i[1])
        if i[0] < 0:
            continue
        if i[0] <= game.player2.x + game.player2.width and (i[1] < game.player2.y + game.player2.height and i[1] + 5 > game.player2.y) \
                and not game.player2.dead:
            game.player2.life -= 1
            if game.player2.life == 0:
                game.player2.dead = True
            continue

        newShots.append(i)

    game.shots1.shotsList = newShots

    if not game.player1.isJump:
        # if keys[pygame.K_UP] and (y1 > vel):
        #     y1 -= vel
        #
        # if keys[pygame.K_DOWN] and (y1 + height + vel < windows_height):
        #     y1 += vel

        if keys[pygame.K_SPACE]:
            game.player1.isJump = True


    else:
        if game.player1.jumpCount >= -10:
            neg = 1
            if game.player1.jumpCount < 0:
                neg = -1
            game.player1.y -= (game.player1.jumpCount ** 2) * 0.5 * neg
            game.player1.jumpCount -= 1

        else:
            game.player1.isJump = False
            game.player1.jumpCount = 10


    drawWindow(game)



pygame.quit()
