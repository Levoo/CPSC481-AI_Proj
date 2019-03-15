import pygame
from pygame.locals import *
from pygame.sprite import Sprite

pygame.init()


window = pygame.display.set_mode((1000, 500))  # set window size


class Player(Sprite):
    def __init__(self):
        self.px = 0
        self.py = 0
        self.speed = 1
        self.p_width = 20
        self.rect = pygame.rect(self.px, self.py, self.p_width, self.p_width)

    def draw_player(self):
        pygame.draw.rect(window, (240, 230, 140), self.rect)  # Draw player every frame


class Wall(Sprite):
    def __init__(self):
        self.p_width = 10
        self.rect = pygame.rect(40, 40, 10, 80)

    def draw_wall(self):
        pygame.draw.rect(window, (240, 140, 230), self.rect)


def check_collision(sprite1, sprite2):
    col = pygame.sprite.collide_rect(sprite1, sprite2)
    if col == True:
        print("Collision")


wall = Wall

main = Player
clock = pygame.time.Clock()
while True:
    clock.tick(120)  # FPS
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

    #check_collision(main, wall)

    window.fill((180, 210, 240))  # draw the background
    # Draw black line       (r,g,b), starting (x,y), ending (x,y), width
    pygame.draw.line(window, (20, 20, 20), (120, 0), (120, 300), 5)

    main.draw_player(main)
    wall.draw_wall(wall)

    pygame.display.update()
