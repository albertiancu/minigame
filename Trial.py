#!/usr/bin/python

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
# standing1 = pygame.image.load('images/character1/char_albert.png')
# standing2 = pygame.image.load('images/character2/L1.png')
#walkLeft1 = [pygame.image.load('images/character1/L1.png'), pygame.image.load('images/character1/L2.png'), pygame.image.load('images/character1/L3.png'),
 #             pygame.image.load('images/character1/L4.png'), pygame.image.load('images/character1/L5.png'), pygame.image.load('images/character1/L6.png'),
  #            pygame.image.load('images/character1/L7.png'), pygame.image.load('images/character1/L8.png'), pygame.image.load('images/character1/L9.png')]
walkLeft1 = [pygame.image.load('images/character1/char_albert_left.png'), pygame.image.load('images/character1/char_albert_left.png'), pygame.image.load('images/character1/char_albert_left.png'),
             pygame.image.load('images/character1/char_albert_left.png'), pygame.image.load('images/character1/char_albert_left.png'), pygame.image.load('images/character1/char_albert_left.png'),
             pygame.image.load('images/character1/char_albert_left.png'), pygame.image.load('images/character1/char_albert_left.png'), pygame.image.load('images/character1/char_albert_left.png')]
#walkRight1 = [pygame.image.load('images/character1/R1.png'), pygame.image.load('images/character1/R2.png'), pygame.image.load('images/character1/R3.png'),
 #             pygame.image.load('images/character1/R4.png'), pygame.image.load('images/character1/R5.png'), pygame.image.load('images/character1/R6.png'),
  #            pygame.image.load('images/character1/R7.png'), pygame.image.load('images/character1/R8.png'), pygame.image.load('images/character1/R9.png')]
walkRight1 = [pygame.image.load('images/character1/char_albert_right.png'), pygame.image.load('images/character1/char_albert_right.png'),pygame.image.load('images/character1/char_albert_right.png'),
              pygame.image.load('images/character1/char_albert_right.png'),pygame.image.load('images/character1/char_albert_right.png'),pygame.image.load('images/character1/char_albert_right.png'),
              pygame.image.load('images/character1/char_albert_right.png'), pygame.image.load('images/character1/char_albert_right.png'),pygame.image.load('images/character1/char_albert_right.png')]
walkLeft2 = [pygame.image.load('images/character2/L1.png'), pygame.image.load('images/character2/L2.png'), pygame.image.load('images/character2/L3.png'),
              pygame.image.load('images/character2/L4.png'), pygame.image.load('images/character2/l5.png'), pygame.image.load('images/character2/L6.png'),
              pygame.image.load('images/character2/L7.png'), pygame.image.load('images/character2/L8.png'), pygame.image.load('images/character2/L9.png')]
walkRight2 = [pygame.image.load('images/character2/R1.png'), pygame.image.load('images/character2/R2.png'), pygame.image.load('images/character2/R3.png'),
              pygame.image.load('images/character2/R4.png'), pygame.image.load('images/character2/R5.png'), pygame.image.load('images/character2/R6.png'),
              pygame.image.load('images/character2/R7.png'), pygame.image.load('images/character2/R8.png'), pygame.image.load('images/character2/R9.png')]
player1 = Player(x=700, y=500, width=89, height=120, vel=5, color=(255, 0, 0), life=10, walkLeft=walkLeft1, walkRight=walkRight1, facing='left')
player2 = Player(x=100, y=500, width=89, height=120, vel=5, color=(0, 255, 0), life=10, walkLeft=walkLeft1, walkRight=walkRight1, facing='right')
# shots1 = Shots()
# shots2 = Shots()
game = Game(win, player1, player2,  background='images/backgrounds/ring.jpg')

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
       # game.player1.left = False
      #  game.player1.right = False
        game.player1.walkCount = 0

    if not game.player1.dead and (keys[pygame.K_RSHIFT] or keys[pygame.K_LSHIFT]):
        if time.time() - game.shots1.lastShotTime >= 0.5:
            if game.player1.shots_fired < 3:
                game.shots1 += Shot(game.player1.x, game.player1.y,  game.player1.right, game.player1.alpha)
                game.shots1.lastShotTime = time.time()
                game.player1.shots_fired += 1

    newShots = []
    for i in game.shots1:
        if i.direction:
            i.x =i.x + i.x_speed

        else:
            i.x = i.x - i.x_speed

        if i.y_count >= (-1) * i.max_high:
            neg = 1
            if i.y_count < 0:
                neg = -1
            i.y -= (i.y_count ** 2) * 0.5 * neg
            i.y_count -= 1

        #TODO: CONITUE FROM HERE!!!!
        if i[0] < 0 or i[0] > windows_width:
            continue
        if i[0] <= game.player2.x + game.player2.width and i[0] >= game.player2.x and (i[1] < game.player2.y + game.player2.height and i[1] + 5 > game.player2.y) \
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
            #ame.player1.left = False
           # game.player1.right = False
            game.player1.walkCount = 0



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


    if keys[pygame.K_UP]:
        if game.player1.alpha >= 90:
            pass
        else:
            game.player1.alpha += 2

    if keys[pygame.K_DOWN]:
        if game.player1.alpha <= 0:
            pass
        else:
            game.player1.alpha -= 2


    if keys[pygame.K_a] and (game.player2.x > game.player2.vel):
        game.player2.x -= game.player2.vel
        game.player2.left = True
        game.player2.right = False


    elif keys[pygame.K_d] and (game.player2.x + game.player2.width + game.player2.vel < windows_width):
        game.player2.x += game.player2.vel
        game.player2.left = False
        game.player2.right = True

    else:
        # game.player1.left = False
        #  game.player1.right = False
        game.player2.walkCount = 0

    if not game.player2.dead and keys[pygame.K_TAB]:
        if time.time() - game.shots2.lastShotTime >= 0.5:
            game.shots2.addShot((game.player2.x + 50, game.player2.y + 100, game.player2.right))
            game.shots2.lastShotTime = time.time()

    newShots = []
    for i in game.shots2.shotsList:
        if i[2]:
            i = (i[0] + 25, i[1], True)
        else:
            i = (i[0] - 25, i[1], False)
        if i[0] < 0 or i[0] > windows_width:
            continue
        if i[0]  <= game.player1.x + game.player1.width and i[0] >= game.player1.x and (
                i[1] < game.player1.y + game.player1.height and i[1] + 5 > game.player1.y) \
                and not game.player1.dead:
            game.player1.life -= 1
            if game.player1.life == 0:
                game.player1.dead = True
            continue

        newShots.append(i)

    game.shots2.shotsList = newShots

    if not game.player2.isJump:
        if keys[pygame.K_2]:
            game.player2.isJump = True
            game.player2.walkCount = 0




    else:
        if game.player2.jumpCount >= -10:
            neg = 1
            if game.player2.jumpCount < 0:
                neg = -1
            game.player2.y -= (game.player2.jumpCount ** 2) * 0.5 * neg
            game.player2.jumpCount -= 1

        else:
            game.player2.isJump = False
            game.player2.jumpCount = 10


    if keys[pygame.K_w]:
        if game.player2.alpha >= 90:
            pass
        else:
            game.player2.alpha += 2

    if keys[pygame.K_s]:
        if game.player2.alpha <= 0:
            pass
        else:
            game.player2.alpha -= 2


    drawWindow(game)



pygame.quit()
