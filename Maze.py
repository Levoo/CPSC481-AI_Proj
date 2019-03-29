import pygame
from pygame.locals import *
from pygame.sprite import Group
from Wall import Wall
from Button import Button
from Unit import Unit
import Functions as f

pygame.init()
windowWidth = 1305 # og 305
windowHeight = 800 # og 720

window = pygame.display.set_mode((windowWidth, windowHeight))  # set window size


clock = pygame.time.Clock()
start_button = Button(window, "START", 500, 250)

main = Unit(window)
wall = Wall(window, 0, 0, 800, 20, (0, 0, 0))
wall2 = Wall(window, 40, 20, 20, 400, (0, 0, 0))
wall3 = Wall(window, 0, 440, 800, 20, (0, 0, 0))
wall4 = Wall(window, 0, 40, 20, 400, (0, 0, 0))
wall5 = Wall(window, 120, 20, 20, 400, (0, 0, 0))
wall6 = Wall(window, 80, 40, 20, 400, (0, 0, 0))
wall7 = Wall(window, 160, 200, 20, 240, (0, 0, 0))
wall8 = Wall(window, 140, 20, 40, 160, (0, 0, 0))
wall9 = Wall(window, 200, 40, 20, 380, (0, 0, 0))
wall10 = Wall(window, 240, 240, 20, 200, (0, 0, 0))
wall11 = Wall(window, 240, 20, 20, 200, (0, 0, 0))
maze = Group()
maze.add(wall, wall2, wall3, wall4, wall5, wall6, wall7, wall8, wall9, wall10, wall11)

while True:
    clock.tick(120)  # FPS
    f.check_events(start_button, main)

    main.ai(maze)

    window.fill((51, 51, 51))  # draw the background
    main.draw()
    for block in maze:
        block.draw()
    if not start_button.pressed:
        start_button.draw()

    pygame.display.update()
