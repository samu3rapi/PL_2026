import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 255, 0), (200, 200), 150)
circle(screen, (0, 0, 0), (200, 200), 150, 3)

circle(screen, (255, 255, 255), (140, 160), 30)
circle(screen, (255, 255, 255), (260, 160), 30)
circle(screen, (0, 0, 0), (140, 160), 15)
circle(screen, (0, 0, 0), (260, 160), 15)

line(screen, (0, 0, 0), (100, 110), (170, 145), 8)
line(screen, (0, 0, 0), (300, 110), (230, 145), 8)

polygon(screen, (255, 0, 0), [(150, 260), (250, 260), (270, 290), (200, 310), (130, 290)])
line(screen, (255, 255, 255), (170, 270), (185, 285), 3)
line(screen, (255, 255, 255), (200, 275), (200, 290), 3)
line(screen, (255, 255, 255), (230, 270), (215, 285), 3)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()