import time
import pygame
from functions import *
from our_classes import *



#init
pygame.init()
windows_width = 1000
windows_height = 700
win = pygame.display.set_mode((windows_width, windows_height))
pygame.display.set_caption("First Game")
standing1 = pygame.image.load('images/character1/standing.png')
standing2 = pygame.image.load('images/character2/L1.png')
walkLeft1 = [pygame.image.load('images/character1/L1.png'), pygame.image.load('images/character1/L2.png'), pygame.image.load('images/character1/L3.png'),
              pygame.image.load('images/character1/L4.png'), pygame.image.load('images/character1/L5.png'), pygame.image.load('images/character1/L6.png'),
              pygame.image.load('images/character1/L7.png'), pygame.image.load('images/character1/L8.png'), pygame.image.load('images/character1/L9.png')]
walkRight1 = [pygame.image.load('images/character1/R1.png'), pygame.image.load('images/character1/R2.png'), pygame.image.load('images/character1/R3.png'),
              pygame.image.load('images/character1/R4.png'), pygame.image.load('images/character1/R5.png'), pygame.image.load('images/character1/R6.png'),
              pygame.image.load('images/character1/R7.png'), pygame.image.load('images/character1/R8.png'), pygame.image.load('images/character1/R9.png')]
walkLeft2 = [pygame.image.load('images/character2/L1.png'), pygame.image.load('images/character2/L2.png'), pygame.image.load('images/character2/L3.png'),
              pygame.image.load('images/character2/L4.png'), pygame.image.load('images/character2/l5.png'), pygame.image.load('images/character2/L6.png'),
              pygame.image.load('images/character2/L7.png'), pygame.image.load('images/character2/L8.png'), pygame.image.load('images/character2/L9.png')]
walkRight2 = [pygame.image.load('images/character2/R1.png'), pygame.image.load('images/character2/R2.png'), pygame.image.load('images/character2/R3.png'),
              pygame.image.load('images/character2/R4.png'), pygame.image.load('images/character2/R5.png'), pygame.image.load('images/character2/R6.png'),
              pygame.image.load('images/character2/R7.png'), pygame.image.load('images/character2/R8.png'), pygame.image.load('images/character2/R9.png')]
player1 = Player(x=700, y=600, width=64, height=64, vel=5, color=(255, 0, 0), life=10, walkLeft=walkLeft1, walkRight=walkRight1, standing=standing1)
player2 = Player(x=100, y=600, width=64, height=64, vel=5, color=(0, 255, 0), life=10, walkLeft=walkLeft2, walkRight=walkRight2, standing=standing2)
shots1 = Shots()
shots2 = Shots()
game = Game(win, player1, player2, shots1, shots2, background='images/backgrounds/ring.jpg')

run = True

clock = pygame.time.Clock()

while run:
    #pygame.time.delay(25)
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and (game.player1.x > game.player1.vel):
        game.player1.x -= game.player1.vel
        game.player1.left = True
        game.player1.right = False

    elif keys[pygame.K_RIGHT] and (game.player1.x + game.player1.width + game.player1.vel < windows_width):
        game.player1.x += game.player1.vel
        game.player1.left = False
        game.player1.right = True

    else:
        game.player1.left = False
        game.player1.right = False
        game.player1.walkCount = 0

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
            game.player1.left = False
            game.player1.right = False
            game.player1.walkCount = 0



    else:
        if game.player1.jumpCount >= -8:
            neg = 1
            if game.player1.jumpCount < 0:
                neg = -1
            game.player1.y -= (game.player1.jumpCount ** 2) * 0.5 * neg
            game.player1.jumpCount -= 1

        else:
            game.player1.isJump = False
            game.player1.jumpCount = 8


    drawWindow(game)



pygame.quit()
