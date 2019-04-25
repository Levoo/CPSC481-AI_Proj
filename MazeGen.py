import enum
import random
import time
import os

#  enum for sides, used for self.walls
class sides(enum.Enum):
    top = 0
    bottom = 1
    right = 2
    left = 3

opp_sides = [1, 0, 3, 2]

class singleCell:
    def __init__(self):
        self.beenVisited = False
        self.walls = [True, True, True, True] # list of booleans, see enum class for index meaning
        self.x = None
        self.y = None

    # prints the node in the 2d array and if it has been visited
    def print_node(self):
        print("Node: (" + str(self.x) + ", " + str(self.y) + ")")
        print("Visited: " + str(self.get_visited_status()))
        #  for (wallPresent, side) in zip(self.walls, sides):
        #  print( str(side.name) + " side: " + str(wallPresent))
    
    def set_visited_status(self, visited):
        self.beenVisited = visited
    
    def set_node_coord(self, x, y):
        self.x = x
        self.y = y
    
    def get_visited_status(self):
        return self.beenVisited


class mazeGen:
    def __init__(self, cellObj, size):
        self.mazeSize = size
        self.grid = [[cellObj for x in range(self.mazeSize)] for y in range(self.mazeSize)]  # n by m matrix

    def __init__(self, cellObj):
        self.mazeSize = 3
        self.grid = [ [cellObj for x in range(self.mazeSize)] for y in range(self.mazeSize) ] # n by m matrix currently 5x5
        self.cell_queue = 0
        self.visitedCount = 0

    def depth_first_search_maze_gen(self):
        dfs_stack = []
        i = 0
        j = 0
        start_cell = singleCell()
        start_cell.set_node_coord(0, 0)
        start_cell.set_visited_status(True)
        self.grid[0][0] = start_cell
        dfs_stack.append(self.grid[0][0])       # put first cell in stack
        print_grid(self.grid)
        while self.visitedCount != (self.mazeSize * self.mazeSize) - 1:  # Loop until all cells are visited
            #  if all adjacent nodes are visited, backtrack by popping
            if self.all_adjacent_visited(self.grid[i][j]):
                dfs_stack.pop()
                next_cell = dfs_stack.pop()
            else:
                neighbor_cell, direction = self.get_rand_node(self.grid[i][j])  # get next rand cell, given current cell
                self.grid[i][j].walls[direction] = False
                next_cell = neighbor_cell
                next_cell.walls[opp_sides[direction]] = False
                print ("~~~Current cell direction: " + str(direction))
                print("~~~Next cell direction: " + str(opp_sides[direction]))

            i = next_cell.x
            j = next_cell.y
            self.grid[i][j] = next_cell
            dfs_stack.append(next_cell)  # Add the next cell to the stack
            print_grid(self.grid)

    def get_rand_node(self, cell):
        self.visitedCount += 1
        direction = None
        sideList = [sides.top, sides.bottom, sides.left, sides.right]  # list of potential position to visit
        while len(sideList) > 0:    # Loop until a cell is found that is not out of bounds and not visited yet
            direction = random.randint(0, len(sideList) - 1)
            cell_is_valid = self.is_valid(sideList[direction], cell)
            # print("Is " + sideList[direction].name + " valid? " + str(cell_is_valid))
            if cell_is_valid:
                break


        next_x = cell.x + 0
        next_y = cell.y + 0

        temp_cell = singleCell()
        temp_cell.set_visited_status(True)

        if sideList[direction] == sides.top:  # top
            next_x = cell.x - 1
            next_y = cell.y + 0
            self.grid[cell.x][cell.y].walls[sides.top.value] = False    # Make the current cells top wall false
            temp_cell.walls[sides.bottom.value] = False                 # make the next cells bottom wall false
            # print ("TOP: (" + str(next_x) + "," + str(next_y) + ")")
        if sideList[direction] == sides.bottom:  # bottom
            next_x = cell.x + 1
            next_y = cell.y + 0
            self.grid[cell.x][cell.y].walls[sides.bottom.value] = False # Make the current cells bottom wall false
            temp_cell.walls[sides.top.value] = False                    # Make the next cells top fall false
            # print ("BOT:(" + str(next_x) + "," + str(next_y) + ")")
        if sideList[direction] == sides.right:  # right
            next_x = cell.x + 0
            next_y = cell.y + 1
            self.grid[cell.x][cell.y].walls[sides.right.value] = False  # Make the current cells right wall false
            temp_cell.walls[sides.left.value] = False                   # Make the next cells left wall false
            # print ("RIGHT (" + str(next_x) + "," + str(next_y) + ")")
        if sideList[direction] == sides.left:  # left
            next_x = cell.x + 0
            next_y = cell.y - 1
            self.grid[cell.x][cell.y].walls[sides.left.value] = False
            temp_cell.walls[sides.right.value] = False
            # print ("LEFT: (" + str(next_x) + "," + str(next_y) + ")")

        temp_cell.set_node_coord(next_x, next_y)


        return temp_cell, direction

    def is_valid(self, direction, node):
        node_x = node.x
        node_y = node.y
        #  First check out of bound
        if node_x == 0 and direction == sides.top:
            return False
        if node_x == self.mazeSize - 1 and direction == sides.bottom:
            return False
        if node_y == 0 and direction == sides.left:
            return False
        if node_y == self.mazeSize - 1 and direction == sides.right:
            return False

        #  Check visited status
        if direction == sides.top:
            if self.grid[node_x - 1][node_y].get_visited_status():
                return False
        if direction == sides.bottom:
            if self.grid[node_x + 1][node_y].get_visited_status():
                return False
        if direction == sides.left:
            if self.grid[node_x][node_y - 1].get_visited_status():
                return False
        if direction == sides.right:
            if self.grid[node_x][node_y + 1].get_visited_status():
                return False
        return True


    def all_adjacent_visited(self, node):
        x = node.x
        y = node.y
        if x != 0:
            if not self.grid[x - 1][y].get_visited_status():  # check top
                return False
        if x != self.mazeSize - 1:
            if not self.grid[x + 1][y].get_visited_status():  # check bottom
                return False
        if y != 0:
            if not self.grid[x][y - 1].get_visited_status():  # check left
                return False
        if y != self.mazeSize - 1:
            if not self.grid[x][y + 1].get_visited_status():  # check right
                return False
        return True

    # EOC 

def print_grid(grid):
    for row in grid:
        for e in row:
            if e.get_visited_status():
                print("V", end=' ')  # Visited
            else:
                print("N", end=' ')  # Not Visited

        print('\n')

def print_node_walls(mazee):

    print(" " + "_" * (6))
    for row in mazee.grid:
        print("|", end="")
        for col in row:
            if col.walls[sides.bottom.value] == True:
                print("_", end="")
            if col.walls[sides.bottom.value] == False:
                print(" ", end="")
            if col.walls[sides.right.value] == True:
                print("|", end="")
            if col.walls[sides.right.value] == False:
                print(" ", end="")
            else:
                print(" ", end="")
            #print("x|", end="")
        print("")
    print("******")
    for row in mazee.grid:
        print("~~~~~")
        for col in row:
            print(col.walls)
        print("~~~~~")
            




def print_walls(grid):
    for row in grid:
        for e in row:
            print("----------------")
            print("Top = ", e.walls[0])
            print("Bottom = ", e.walls[1])
            print("Right = ", e.walls[2])
            print("Left = ", e.walls[3])

cells = singleCell()
genn = mazeGen(cells)

genn.depth_first_search_maze_gen()

print_node_walls(genn)
