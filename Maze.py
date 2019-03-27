import pygame
from pygame.locals import *
from pygame.sprite import Sprite
from Button import Button
import Functions as f

pygame.init()


window = pygame.display.set_mode((1000, 500))  # set window size


class Unit(Sprite):
    def __init__(self, window):
        super(Unit, self).__init__()
        self.window = window
        self.speed = 1
        self.p_width = 20
        self.rect = pygame.Rect(0, 0, self.p_width, self.p_width)
        self.last_direction = 'r'
        self.last_position = ''

    def draw(self):
        pygame.draw.rect(self.window, (240, 230, 140), self.rect)  # Draw player every frame


class Wall(Sprite):
    def __init__(self, window):
        super(Wall, self).__init__()
        self.window = window
        self.p_width = 10
        self.rect = pygame.Rect(40, 40, 20, 20)

    def draw(self):
        pygame.draw.rect(window, (240, 140, 230), self.rect)


def check_collision(sprite1, sprite2):
    col = pygame.sprite.collide_rect(sprite1, sprite2)
    if col:
        if sprite1.rect.right < sprite2.rect.x + 3 * sprite1.speed:
            sprite1.rect.right = sprite2.rect.x
        elif sprite1.rect.x > sprite2.rect.right - 3 * sprite1.speed:
            sprite1.rect.x = sprite2.rect.right
        if sprite1.rect.bottom < sprite2.rect.y + 3 * sprite1.speed:
            sprite1.rect.bottom = sprite2.rect.y
        elif sprite1.rect.y > sprite2.rect.bottom - 3 * sprite1.speed:
            sprite1.rect.y = sprite2.rect.bottom


wall = Wall(window)

main = Unit(window)
clock = pygame.time.Clock()
start_button = Button(window, "START", 500, 250)

while True:
    clock.tick(120)  # FPS
    f.check_events(start_button, main)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        main.rect.x -= main.speed
    if keys[pygame.K_RIGHT]:
        main.rect.x += main.speed
    if keys[K_UP]:
        main.rect.y -= main.speed
    if keys[K_DOWN]:
        main.rect.y += main.speed

    check_collision(main, wall)

    window.fill((180, 210, 240))  # draw the background
    # Draw black line       (r,g,b), starting (x,y), ending (x,y), width
    pygame.draw.line(window, (20, 20, 20), (120, 0), (120, 300), 5)

    main.draw()
    wall.draw()
    start_button.draw()

    pygame.display.update()
