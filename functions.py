import pygame

def text_to_screen(screen, text, x, y, color = (255, 255, 255), size = 20):
    font = pygame.font.SysFont("comicsansms", size)
    text = font.render(text, True, color)
    screen.blit(text,(x, y))


def drawWindow():
    win.fill((0, 0, 0))  # Fills the screen with black
    player1.draw(win)
    computer.draw(win)
    for i in shots:
        pygame.draw.rect(win, (0, 0, 255), (i[0], i[1], 10, 10))

    text_to_screen(win, 'computer life: ' + str(computer.life), 10, 10)

    pygame.display.update()
