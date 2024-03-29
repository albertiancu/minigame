import pygame
from GlobalParameters import *


def text_to_screen(screen, text, x, y, color = (255, 255, 255), size = 20):
    font = pygame.font.SysFont("comicsansms", size)
    text = font.render(text, True, color)
    screen.blit(text,(x, y))


def drawWindow(game):
    if game.background is None:
        game.win.fill((0, 0, 0))  # Fills the screen with black

    else:
        game.win.blit(game.background, (0,0))
        
    game.player1.draw(game.win)
    game.player2.draw(game.win)
    for i in game.shots1.shotsList:
       # game.win.blit(pygame.image.load('images/character1/mamaliga.png'), (i[0],i[1] + 60))
        pygame.draw.circle(game.win, (255, 249, 140), (int(i[0]), int(i[1])), 10)

    for i in game.shots2.shotsList:
        pygame.draw.circle(game.win, (255, 255, 255), (int(i[0]), int(i[1])), 10)


    if game.player1.dead and game.player2.dead:
        text_to_screen(game.win, "DRAW!", 300, 200, size=80)

    elif game.player1.dead:
        text_to_screen(game.win, "Player2 Won!", 175, 200, size=80)
        text_to_screen(game.win, "player2's life: " + str(game.player2.life), 10, 10)

    elif game.player2.dead:
        text_to_screen(game.win, "Player1 Won!", 170, 200, size=80)
        text_to_screen(game.win, "player1's life: " + str(game.player1.life), 800, 10)


    else:
        text_to_screen(game.win, "player2's life: " + str(game.player2.life), 10, 10)
        text_to_screen(game.win, "player1's life: " + str(game.player1.life), 800, 10)

    pygame.display.update()
