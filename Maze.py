import pygame
from pygame.locals import *
from pygame.sprite import Group
from Wall import Wall
from Button import Button
from Unit import Unit
import Functions as f
from MazeGen import *
from NodeGen import *
import random

pygame.init()
windowWidth = 1205 # og 305
windowHeight = 850 # og 720

window = pygame.display.set_mode((windowWidth, windowHeight))  # set window size


clock = pygame.time.Clock()
start_button = Button(window, "START", 500, 250)

mazeWidth = 16
col = (100, 100, 100)

gridsize = 10
cells = singleCell()
genn = mazeGen(cells, gridsize)
genn.depth_first_search_maze_gen()
nodes = []
pop_no = 10
genNode(genn.grid, gridsize, nodes, pop_no)      # Determine which cells are nodes
genNeighbor(genn.grid, gridsize)  # Get the neighbors for each node in grid

colors = []
for x in range(pop_no):
    if x / pop_no < 0.2:
        colors.append((255, 255 * (x / pop_no / 0.2), 0))
    elif x / pop_no < 0.4:
        colors.append((255 * (1 - (x / pop_no / 0.4)), 255, 0))
    elif x / pop_no < 0.6:
        colors.append((0, 255, 255 * (x / pop_no / 0.6)))
    elif x / pop_no < 0.8:
        colors.append((0, 255 * (1 - (x / pop_no / 0.8)), 255))
    elif x / pop_no <= 1:
        colors.append((255 * (x / pop_no), 0, 255))
candidates = [Unit(window, mazeWidth, nodes[0], x, colors[x]) for x in range(pop_no)]

grid_arr = []       # array of Wall objects
node_arr = []

for i in range(gridsize):
    for j in range(gridsize):
        # For every cell, if wall is true then draw wall
        # Make Left Walls
        if genn.grid[j][i].walls[sides.left.value] is True:
            tempLeft = Wall(window, (i * mazeWidth*2), (j * mazeWidth*2), mazeWidth, mazeWidth*3, col)
            grid_arr.append(tempLeft)

        # Make Right Walls
        if genn.grid[j][i].walls[sides.right.value] is True:
            tempRight = Wall(window, ((i * mazeWidth*2) + mazeWidth*2), (j * mazeWidth*2), mazeWidth, mazeWidth*3, col)
            grid_arr.append(tempRight)

        # Make Top Walls
        if genn.grid[j][i].walls[sides.top.value] is True:
            tempTop = Wall(window, (i * mazeWidth*2), (j * mazeWidth*2), mazeWidth*3, mazeWidth, col)
            grid_arr.append(tempTop)

        # Make Bottom Walls
        if genn.grid[j][i].walls[sides.bottom.value] is True:
            tempBottom = Wall(window, (i * mazeWidth*2), ((j * mazeWidth*2) + mazeWidth*2), mazeWidth*3, mazeWidth, col)
            grid_arr.append(tempBottom)

        if genn.grid[j][i].isNode is True:
            box = ((i * (mazeWidth*2)) + (mazeWidth + mazeWidth/4), (j * (mazeWidth*2)) + (mazeWidth + mazeWidth/4), mazeWidth/2, mazeWidth/2)
            node_arr.append(box)


grid = Group()
grid.add(grid_arr)


def drawNode(s, c, r):
    pygame.draw.rect(s, c, r)


while True:
    clock.tick(120)  # FPS

    f.check_events(start_button)

    window.fill((51, 51, 51))  # draw the background

    for x in reversed(candidates):
        x.ai()
        x.draw()

    for block in grid:
        block.draw()

    for n in node_arr:
        drawNode(window, (255, 255, 255), n)

    pygame.display.update()
