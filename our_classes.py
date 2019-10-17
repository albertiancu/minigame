import pygame
import time
class Shots(object):
    def __init__(self):
        self.shotsList = []
        self.lastShotTime = time.time()

    def addShot(self, other):
        self.shotsList.append(other)


class Game(object):
    def __init__(self, win, player1, player2, shots1, shots2):
        self.win = win
        self.player1 = player1
        self.player2 = player2
        self.shots1 = shots1
        self.shots2 = shots2

class Player(object):
    def __init__(self, x, y, width, height, vel, color, life):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel #speed (how many pixels the player move every step)
        self.isJump = False
        self.jumpCount = 10 #acceleration
        self.dead = False
        self.color = color
        self.life = life

    def draw(self, win):
        if not self.dead:
            pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))


#
# class balls(object):
#     def __init__(self):
#         self.shot = []
#
#     def __init__(self, array):
#         self.shot = array


