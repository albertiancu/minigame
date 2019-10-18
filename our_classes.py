import pygame
import time
#eara
class Shots(object):
    def __init__(self):
        self.shotsList = []
        self.lastShotTime = time.time()

    def addShot(self, other):
        self.shotsList.append(other)


class Shot(object):
    def __init__(self, x, y, direction, alpha):
        self.x = x
        self.y = y
        self.direction = direction
        self.x_speed = 100//(alpha+1)
        self.y_count = alpha//10
        self.max_high = alpha//10



class Game(object):
    def __init__(self, win, player1, player2, background):
        self.win = win
        self.player1 = player1
        self.player2 = player2
        self.shots1 = []
        self.shots2 = []
        self.background = pygame.image.load(background)



class Player(object):
    def __init__(self, x, y, width, height, vel, color, life, walkLeft, walkRight, facing):
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

        self.shots_fired = 0

        self.alpha = 0


        self.walkLeft = walkLeft
        self.walkRight = walkRight
        if facing == 'left':
            self.left = True
            self.right = False
        elif facing == 'right':
            self.left = False
            self.right = True
        self.walkCount = 0



    def draw(self, win):
        if not self.dead:

            if self.walkCount >= 27:
                self.walkCount = 0

            if self.left:
                # rotated = pygame.transform.rotate(self.walkRight[self.walkCount // 3], 0)
                # win.blit(rotated, (self.x, self.y))
                blitRotateCenter(win, self.walkLeft[self.walkCount // 3], (self.x, self.y), (-1)*self.alpha)
                self.walkCount += 1

            elif self.right:
                # rotated = pygame.transform.rotate(self.walkRight[self.walkCount // 3], 30)
                # win.blit(rotated, (self.x, self.y))
                blitRotateCenter(win, self.walkRight[self.walkCount // 3], (self.x, self.y), self.alpha)
                #win.blit(self.walkRight[self.walkCount // 3], (self.x, self.y))
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


def blitRotateCenter(surf, image, topleft, angle):

    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(topleft = topleft).center)

    surf.blit(rotated_image, new_rect.topleft)