import pygame
from pygame.locals import *

pygame.init()


window = pygame.display.set_mode((1000, 500))

class Player:
    px = 0
    py = 0
    speed = 1
    pwid = 20

main = Player
clock = pygame.time.Clock()
while True:
    clock.tick(120)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        main.px -= main.speed
    if keys[pygame.K_RIGHT]:
        main.px += main.speed
    if keys[K_UP]:
        main.py -= main.speed
    if keys[K_DOWN]:
        main.py += main.speed

    if main.px == 98 and main.py < 300:
        main.px = 97
    if main.px == 123 and main.py < 300:
        main.px = 124


    window.fill((180, 210, 240))
    pygame.draw.line(window, (20, 20, 20), (120, 0), (120, 300), 5)
    pygame.draw.rect(window, (240, 230, 140), (main.px, main.py, main.pwid, main.pwid))

    pygame.display.update()
