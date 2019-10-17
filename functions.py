import pygame
from GlobalParameters import *


def text_to_screen(screen, text, x, y, color = (255, 255, 255), size = 20):
    font = pygame.font.SysFont("comicsansms", size)
    text = font.render(text, True, color)
    screen.blit(text,(x, y))


def drawWindow(game):
    game.win.fill((0, 0, 0))  # Fills the screen with black
    game.player1.draw(game.win)
    game.player2.draw(game.win)
    for i in game.shots1.shotsList:
        pygame.draw.rect(game.win, (0, 0, 255), (i[0], i[1], 10, 10))

    text_to_screen(game.win, 'computer life: ' + str(game.player2.life), 10, 10)

    pygame.display.update()
