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
windowHeight = 850 # og 720

window = pygame.display.set_mode((windowWidth, windowHeight))  # set window size


clock = pygame.time.Clock()
start_button = Button(window, "START", 500, 250)

mazeWidth = 16
main = Unit(window, mazeWidth)
col = (105, 180, 190)

gridsize = 20
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
            tempLeft = Wall(window, (i * mazeWidth*2), (j * mazeWidth*2), mazeWidth, mazeWidth*3, col)
            grid_arr.append(tempLeft)

        # Make Right Walls
        if genn.grid[j][i].walls[sides.right.value] == True:
            tempRight = Wall(window, ((i * mazeWidth*2) + mazeWidth*2), (j * mazeWidth*2), mazeWidth, mazeWidth*3, col)
            grid_arr.append(tempRight)

        # Make Top Walls
        if genn.grid[j][i].walls[sides.top.value] == True:
            tempTop = Wall(window, (i * mazeWidth*2), (j * mazeWidth*2), mazeWidth*3, mazeWidth, col)
            grid_arr.append(tempTop)

        # Make Bottom Walls
        if genn.grid[j][i].walls[sides.bottom.value] == True:
            tempBottom = Wall(window, (i * mazeWidth*2), ((j * mazeWidth*2) + mazeWidth*2), mazeWidth*3, mazeWidth, col)
            grid_arr.append(tempBottom)

        if genn.grid[j][i].isNode == True:
            box = ((i * (mazeWidth*2)) + (mazeWidth + mazeWidth/4), (j * (mazeWidth*2)) + (mazeWidth + mazeWidth/4), mazeWidth/2, mazeWidth/2)
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
        drawNode(window, (255, 255, 255), n)

    pygame.display.update()