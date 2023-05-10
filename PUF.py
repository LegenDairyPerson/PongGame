import pygame
win = pygame.display.set_mode((400, 400))


def addtext(message, xpos, ypos, colorx, givenfont=None, fontsize=32):
    font1 = pygame.font.SysFont(givenfont, fontsize)
    text = font1.render(message, True, colorx, None)
    textrect = text.get_rect()
    textrect.topleft = xpos, ypos
    win.blit(text, textrect)


def addimage(image, xpos, ypos, width: int = 100, height: int = 100):
    image1 = pygame.image.load(image)
    image = pygame.transform.scale(image1, (width, height))
    win.blit(image, (xpos, ypos))
