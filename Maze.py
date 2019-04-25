import pygame
from pygame.locals import *
from pygame.sprite import Group
from Wall import Wall
from Button import Button
from Unit import Unit
import Functions as f
from MazeGen import *

pygame.init()
windowWidth = 1305 # og 305
windowHeight = 800 # og 720

window = pygame.display.set_mode((windowWidth, windowHeight))  # set window size


clock = pygame.time.Clock()
start_button = Button(window, "START", 500, 250)

main = Unit(window)
col = (144, 231, 192)
gridsize = 10
cells = singleCell()
genn = mazeGen(cells, gridsize)
genn.depth_first_search_maze_gen()
grid_arr = []       # array of Wall objects

for i in range(gridsize):
    for j in range(gridsize):
        # For every cell, if wall is true then draw wall
        # Make Left Walls
        if genn.grid[j][i].walls[sides.left.value] == True:
            tempLeft = Wall(window, (i * 40), (j * 40), 20, 60, col)
            grid_arr.append(tempLeft)

        # Make Right Walls
        if genn.grid[j][i].walls[sides.right.value] == True:
            tempRight = Wall(window, ((i * 40) + 40), (j * 40), 20, 60, col)
            grid_arr.append(tempRight)

        # Make Top Walls
        if genn.grid[j][i].walls[sides.top.value] == True:
            tempTop = Wall(window, (i * 40), (j * 40), 60, 20, col)
            grid_arr.append(tempTop)

        # Make Bottom Walls
        if genn.grid[j][i].walls[sides.bottom.value] == True:
            tempBottom = Wall(window, (i * 40), ((j * 40) + 40), 60, 20, col)
            grid_arr.append(tempBottom)

grid = Group()
grid.add(grid_arr)

while True:
    clock.tick(120)  # FPS
    f.check_events(start_button, main)

    main.ai(grid)

    window.fill((51, 51, 51))  # draw the background
    main.draw()

    for block in grid:
        block.draw()

    pygame.display.update()
