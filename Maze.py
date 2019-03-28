import pygame
from pygame.locals import *
from pygame.sprite import Group
from Wall import Wall
from Button import Button
from Unit import Unit
import Functions as f

pygame.init()


window = pygame.display.set_mode((1000, 500))  # set window size


clock = pygame.time.Clock()
start_button = Button(window, "START", 500, 250)

main = Unit(window)
wall = Wall(window, 40, 40, 80, 80, (0, 0, 0))
maze = Group()
maze.add(wall)

while True:
    clock.tick(120)  # FPS
    f.check_events(start_button, main)

    main.check_collision(maze)

    window.fill((51, 51, 51))  # draw the background
    # Draw black line       (r,g,b), starting (x,y), ending (x,y), width
    pygame.draw.line(window, (20, 20, 20), (120, 0), (120, 300), 5)

    main.draw()
    wall.draw()
    start_button.draw()

    pygame.display.update()
