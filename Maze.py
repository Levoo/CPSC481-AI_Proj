import pygame
from pygame.locals import *
from pygame.sprite import Group
from Wall import Wall
from Button import Button
from Unit import Unit
import Functions as f
from MazeGen import *
from NodeGen import genNode
import random

pygame.init()
windowWidth = 1205 # og 305
windowHeight = 650 # og 720

window = pygame.display.set_mode((windowWidth, windowHeight))  # set window size


clock = pygame.time.Clock()
start_button = Button(window, "START", 500, 250)

main = Unit(window)
col = (55, 140, 130)


gridsize = 15
cells = singleCell()
genn = mazeGen(cells, gridsize)
genn.depth_first_search_maze_gen()
genNode(genn.grid, gridsize)
grid_arr = []       # array of Wall objects
node_arr = []

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

        if genn.grid[j][i].isNode == True:
            box = ((i * 40) + 25, (j * 40) + 25, 10, 10)
            node_arr.append(box)


grid = Group()
grid.add(grid_arr)

def drawNode(s, c, r):
    pygame.draw.rect(s, c, r)

while True:
    clock.tick(120)  # FPS
    f.check_events(start_button, main)

    main.ai(grid)

    window.fill((51, 51, 51))  # draw the background
    main.draw()

    for block in grid:
        block.draw()

    for n in node_arr:
        drawNode(window, (0, 130, 240), n)

    pygame.display.update()