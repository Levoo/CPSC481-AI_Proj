import enum
import random

class sides(enum.Enum):
    top = 0
    bottom = 1
    right = 2
    left = 3

class singleCell:
    def __init__(self):
        self.hasBeenVisited = False
        self.walls = [] # list of booleans, see enum class for index meaning
    def set_visited(self, visited): 
        print("Changed visited status to visited")
        self.hasBeenVisited = visited

class mazeGen:
    def __init__(self, cellObj):
        self.grid = [ [cellObj for x in range(5)] for y in range(5) ] # n by m matrix currently 5x5
        self.cell_queue = 0
        self.visitedCount = 0
    def print_list(self):
        for row in self.grid:
            for nexxt in row:
                print(nexxt)
                print("------------------")
    def depth_first_search_maze_gen(self):
        x, y = self.get_rand_node()
        print ("X: " + str(x) + "| Y: " + str(y))
        print(self.grid[x][y])
        self.grid[x][y].set_visited(True)

    def get_rand_node(self):
        return random.randint(0,4), random.randint(0,4)

cells = singleCell()
genn = mazeGen(cells)

genn.depth_first_search_maze_gen()