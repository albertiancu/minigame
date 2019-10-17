import pygame
import time
#eara
class Shots(object):
    def __init__(self):
        self.shotsList = []
        self.lastShotTime = time.time()

    def addShot(self, other):
        self.shotsList.append(other)


class Game(object):
    def __init__(self, win, player1, player2, shots1, shots2, background):
        self.win = win
        self.player1 = player1
        self.player2 = player2
        self.shots1 = shots1
        self.shots2 = shots2
        self.background = pygame.image.load(background)

class Player(object):
    def __init__(self, x, y, width, height, vel, color, life, walkLeft, walkRight, standing):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel #speed (how many pixels the player move every step)
        self.isJump = False
        self.jumpCount = 8 #acceleration
        self.dead = False
        self.color = color
        self.life = life
        self.walkLeft = walkLeft
        self.walkRight = walkRight
        self.standing = standing
        self.left = True
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if not self.dead:

            if self.walkCount >= 27:
                self.walkCount = 0

            if self.left:
                win.blit(self.walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            elif self.right:
                win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            else:
                win.blit(self.standing, (self.x, self.y))


            #pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


#
# class balls(object):
#     def __init__(self):
#         self.shot = []
#
#     def __init__(self, array):
#         self.shot = array


