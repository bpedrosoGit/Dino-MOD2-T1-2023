import pygame
from Chaves_Runner.components.game import *
pygame.init()
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1100
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Launcher.exe")
drawBg = pygame.transform.scale(pygame.image.load('Chaves_Runner/assets/background/Menu.png'), (SCREEN_WIDTH, SCREEN_HEIGHT))
imgBtn = pygame.image.load("Chaves_Runner/assets/background/Jogar.png")
clicked = False



launcher = True
while launcher:
    posx, posy = pygame.mouse.get_pos()
    screen.blit(drawBg, (0,0))
    screen.blit(imgBtn, (500,450))

    if (posx > 500 and posx < 660) and (posy > 450 and posy < 530):
        if clicked == True:
            insideMenu()
    clicked = False
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicked = True

    pygame.display.flip()