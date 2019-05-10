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
import sys

pygame.init()
windowWidth = 738 # og 305
windowHeight = 404 # og 720

window = pygame.display.set_mode((windowWidth, windowHeight))  # set window size
pygame.display.set_caption("Pseudo-genetic maze navigator")


clock = pygame.time.Clock()
start_button = Button(window, "START", 360, 275, 200, 50)
quit_button = Button(window, "QUIT", 360, 350, 200, 50)
increase_button = Button(window, "+", 428, 225, 25, 25)
decrease_button = Button(window, "-", 294, 225, 25, 25)


mazeWidth = 16
col = (100, 100, 100)

gridsize = 10
cells = singleCell()
genn = mazeGen(cells, gridsize)
genn.depth_first_search_maze_gen()
nodes = []
parents = []
genes = []
pop_no = 10
generations = 3
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

candidates = [Unit(window, mazeWidth, nodes[0], x, colors[x], []) for x in range(pop_no)]

grid_arr = []       # array of Wall objects
node_arr = []
end_node_options = {}
end_node_index = None

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
            if (j  == (gridsize - 3) or j  == (gridsize - 2) or j  == (gridsize - 1)):#\
                #or (i  == (gridsize - 3) or i  == (gridsize - 2) or i  == (gridsize - 1)) :
                end_node_options[len(node_arr)] = [j, i]
            node_arr.append(box)

end_node_index = genn.set_maze_end(end_node_options)
grid = Group()
grid.add(grid_arr)


def drawNode(s, c, r):
    pygame.draw.rect(s, c, r)


def new_candidates():
    genes.clear()
    z = 0
    while z < len(parents[0].visited_nodes) and z < len(parents[1].visited_nodes) and parents[0].visited_nodes[z] == \
            parents[1].visited_nodes[z]:
        genes.append(parents[0].visited_nodes[z])
        z += 1
    candidates.clear()
    parents[0].reset(nodes[0])
    parents[0].id_no = 0
    parents[0].color = colors[0]
    candidates.append(parents[0])
    parents[1].reset(nodes[0])
    parents[1].id_no = 1
    parents[1].color = colors[1]
    candidates.append(parents[1])
    parents.clear()
    for x in range(2, pop_no - 1):
        candidates.append(Unit(window, mazeWidth, nodes[0], x, colors[x], genes))
        if len(genes) > 1:
            genes.pop()
    candidates.append(Unit(window, mazeWidth, nodes[0], pop_no - 1, colors[pop_no - 1], []))
    for node in nodes:
        node.beenVisited.clear()
        node.check_out.clear()
        node.beenVisited = [(False, None) for x in range(pop_no)]
        node.check_out = [{"up": False, "down": False, "left": False, "right": False} for x in range(pop_no)]


def draw_stats():
    rect = pygame.Rect(0, 342, 0, 0)
    font1 = pygame.font.SysFont(None, 36)
    window.blit(font1.render("Generation: " + str(gen_count), True, (255, 255, 255), (51, 51, 51)), rect)
    rect = rect.move(0, 36)
    if gen_count < generations - 1:
        window.blit(font1.render("Parents =", True, (255, 255, 255), (51, 51, 51)), rect)
    rect = rect.move(342, -378)
    font1.set_underline(True)
    window.blit(font1.render("Candidates", True, (255, 255, 255), (51, 51, 51)), rect)
    rect = rect.move(180, 0)
    window.blit(font1.render("Weight", True, (255, 255, 255), (51, 51, 51)), rect)
    font1.set_underline(False)
    for candidate in candidates:
        rect = pygame.Rect(342, 32 + 32 * candidate.id_no, mazeWidth, mazeWidth)
        pygame.draw.rect(window, candidate.color, rect)
        rect = rect.move(180, 0)
        if candidate.finished is False:
            window.blit(font1.render(str(int(candidate.weight)), True, (255, 255, 255), (51, 51, 51)), rect)
        else:
            window.blit(font1.render(str(int(candidate.weight)), True, (221, 188, 0), (51, 51, 51)), rect)
    if gen_count < generations - 1:
        if len(parents) > 0:
            rect = pygame.Rect(118, 384, mazeWidth, mazeWidth)
            pygame.draw.rect(window, parents[0].color, rect)
            if len(parents) > 1:
                rect = rect.move(36, 0)
                pygame.draw.rect(window, parents[1].color, rect)


print("Start")
while True:
    clock.tick(120)  # FPS

    f.check_events(start_button, quit_button, increase_button, decrease_button)

    if increase_button.pressed:
        generations += 1
        increase_button.pressed = False
    elif decrease_button.pressed and generations > 1:
        generations -= 1
        decrease_button.pressed = False

    window.fill((51, 51, 51))  # draw the background

    font = pygame.font.SysFont(None, 72)
    rect = pygame.Rect(144, 36, 99, 36)
    window.blit(font.render("PSEUDO-GENETIC", True, (255, 255, 255), (51, 51, 51)), rect)
    rect = rect.move(0, 54)
    window.blit(font.render("MAZE NAVIGATOR", True, (255, 255, 255), (51, 51, 51)), rect)
    font = pygame.font.SysFont(None, 24)
    rect = rect.move(-18, 72)
    window.blit(font.render("By: Arnold Ruiz, Fernando Cuevas, Alex Ma, Ye-Rham Hwang", True, (255, 255, 255), (51, 51, 51)), rect)
    rect = rect.move(186, 27)
    window.blit(font.render("Generations", True, (255, 255, 255), (51, 51, 51)), rect)
    rect = rect.move(0, 18)
    pygame.draw.rect(window, (25, 25, 25), rect)
    if generations < 10:
        rect = rect.move(44, 9)
        window.blit(font.render(str(generations), True, (255, 255, 255), (25, 25, 25)), rect)
    else:
        rect = rect.move(40, 9)
        window.blit(font.render(str(generations), True, (255, 255, 255), (25, 25, 25)), rect)

    start_button.draw()
    quit_button.draw()
    increase_button.draw()
    decrease_button.draw()

    if start_button.pressed:
        gen_count = 0
        while gen_count < generations:
            while len(parents) < pop_no:
                clock.tick(120)  # FPS

                for event in pygame.event.get():
                    if event.type == pygame.QUIT or quit_button.pressed:
                        print("")
                        sys.exit()
                window.fill((51, 51, 51))  # draw the background

                for x in reversed(candidates):
                    x.ai(parents)
                    x.draw()

                for block in grid:
                    block.draw()

                counter = 0
                node_array_size = len(node_arr) - 1
                for n in node_arr:
                    if end_node_index == counter:
                        drawNode(window, (144, 51, 115), n)
                    elif counter == 0:
                        drawNode(window, (188, 188, 0), n)
                    else:
                        drawNode(window, (255, 255, 255), n)
                    counter = counter + 1

                draw_stats()
                pygame.display.update()
                pygame.time.delay(5)
            pause = 0
            font = pygame.font.SysFont(None, 36)
            while pause < 360:
                clock.tick(120)
                pause += 1



            new_candidates()
            gen_count += 1

        start_button.press = False
        start_button.pressed = False
        nodes.clear()
        genn = mazeGen(cells, gridsize)
        genn.depth_first_search_maze_gen()
        grid_arr.clear()
        node_arr.clear()
        end_node_options = {}
        end_node_index = None
        genNode(genn.grid, gridsize, nodes, pop_no)  # Determine which cells are nodes
        genNeighbor(genn.grid, gridsize)  # Get the neighbors for each node in grid

        for i in range(gridsize):
            for j in range(gridsize):
                # For every cell, if wall is true then draw wall
                # Make Left Walls
                if genn.grid[j][i].walls[sides.left.value] is True:
                    tempLeft = Wall(window, (i * mazeWidth * 2), (j * mazeWidth * 2), mazeWidth, mazeWidth * 3, col)
                    grid_arr.append(tempLeft)

                # Make Right Walls
                if genn.grid[j][i].walls[sides.right.value] is True:
                    tempRight = Wall(window, ((i * mazeWidth * 2) + mazeWidth * 2), (j * mazeWidth * 2), mazeWidth,
                                     mazeWidth * 3, col)
                    grid_arr.append(tempRight)

                # Make Top Walls
                if genn.grid[j][i].walls[sides.top.value] is True:
                    tempTop = Wall(window, (i * mazeWidth * 2), (j * mazeWidth * 2), mazeWidth * 3, mazeWidth, col)
                    grid_arr.append(tempTop)

                # Make Bottom Walls
                if genn.grid[j][i].walls[sides.bottom.value] is True:
                    tempBottom = Wall(window, (i * mazeWidth * 2), ((j * mazeWidth * 2) + mazeWidth * 2), mazeWidth * 3,
                                      mazeWidth, col)
                    grid_arr.append(tempBottom)

                if genn.grid[j][i].isNode is True:
                    box = ((i * (mazeWidth * 2)) + (mazeWidth + mazeWidth / 4),
                           (j * (mazeWidth * 2)) + (mazeWidth + mazeWidth / 4), mazeWidth / 2, mazeWidth / 2)
                    if (j == (gridsize - 3) or j == (gridsize - 2) or j == (gridsize - 1)):  # \
                        # or (i  == (gridsize - 3) or i  == (gridsize - 2) or i  == (gridsize - 1)) :
                        end_node_options[len(node_arr)] = [j, i]
                    node_arr.append(box)

        end_node_index = genn.set_maze_end(end_node_options)
        grid.empty()
        grid.add(grid_arr)
        candidates = [Unit(window, mazeWidth, nodes[0], x, colors[x], []) for x in range(pop_no)]

    pygame.display.update()
