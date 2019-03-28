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
wall = Wall(window)
maze = Group()
maze.add(wall)

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

    main.check_collision(maze)

    window.fill((180, 210, 240))  # draw the background
    # Draw black line       (r,g,b), starting (x,y), ending (x,y), width
    #pygame.draw.line(window, (20, 20, 20), (120, 0), (120, 300), 5)

    main.draw()
    wall.draw()

    # vertical lines
    for x in range(0, 1305, 50):
        wall.draw(pygame.Rect(x, 0, 5, 705))
        #print("placing line on x: " + str(x))
    # horizontal lines
    for y in range(0, 720, 50):
        wall.draw(pygame.Rect(0, y, 1305, 5))
        #print("placing line on x: " + str(x))

    #draw outline of maze
    #wall.create_maze_outline(windowWidth, windowHeight)
    #start_button.draw()

    pygame.display.update()
