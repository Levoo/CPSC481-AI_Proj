import enum
import random
import queue

# WIP

'''
for later

for x in range(0, 1305, 50):
        wall.draw(pygame.Rect(x, 0, 5, 705))
        #print("placing line on x: " + str(x))
    # horizontal lines
    for y in range(0, 720, 50):
        wall.draw(pygame.Rect(0, y, 1305, 5))
        #print("placing line on x: " + str(x))

'''





#enum for sides, used for self.walls 
class sides(enum.Enum):
    top = 0
    bottom = 1
    right = 2
    left = 3

class singleCell:
    def __init__(self):
        self.beenVisited = False
        self.walls = [True, True, True, True] # list of booleans, see enum class for index meaning
        self.x = None
        self.y = None
    # prints the node in the 2d array and if it has been visited, 
    def print_node(self):
        print("Node: (" + str(self.x) +", "  + str(self.y) + ")")
        print("Visited: " + str(self.get_visited_status()))
        for (wallPresent, side) in zip(self.walls, sides):
            print( str(side.name) + " side: " + str(wallPresent)) 
    
    def set_visited_status(self, visited): 
        print("Changed visited status to visited")
        self.beenVisited = visited
    
    def set_node_coord(self, x, y):
        self.x = x
        self.y = y
    
    def get_visited_status(self):
        return self.beenVisited

class mazeGen:
    def __init__(self, cellObj):
        self.size = 5
        self.grid = [ [cellObj for x in range(self.size)] for y in range(self.size) ] # n by m matrix currently 5x5
        self.cell_queue = 0
        self.visitedCount = 0

    '''
    Implement psedo-code: WIP
    Randomly select a node (or cell) N.
    Push the node N onto a queue Q.
    Mark the cell N as visited.
    Randomly select an adjacent cell A of node N that has not been visited. If all the neighbors of N have been visited:
        Continue to pop items off the queue Q until a node is encountered with at least one non-visited neighbor - assign this node to N and go to step 4.
        If no nodes exist: stop.
    Break the wall between N and A.
    Assign the value A to N.
    Go to step 2.
    '''
    def depth_first_search_maze_gen(self):
        dfsQ = queue.Queue(maxsize=self.size*self.size)

        i = 0
        j = 0
        self.grid[0][0].set_node_coord(0, 0)  # starting cell is at (0, 0)
        self.grid[0][0].set_visited_status(True)
        dfsQ.put(self.grid[0][0])               # put first cell in queue
        while self.visitedCount != (self.size * self.size):
            currentCell = self.grid[i][j]
            #  TODO: make a function that returns bool if all adjacent nodes are visited
            #  if bool = true, then pop queue with: dfsQ.get(self.grid[i][j] and exit current loop
            #  else:
            nextCell = self.get_rand_node(currentCell)  # get next rand cell, given current cell
            dfsQ.put(nextCell)
            i = nextCell.x
            j = nextCell.y

    #  TODO: Find a way to remove visited cells from random pool
    #  Ex. If bottom is visited, find a way so that 1 (bottom) cant be randomly selected
    #  TODO: Check for out of bounds ex, if at top level, top should not be chosen

    def get_rand_node(self, cell):

        direction = random.randint(0, 3)
        if direction == 0:  # top
            nextX = cell.x + 0
            nextY = cell.y + 1
        if direction == 1:  # bottom
            nextX = cell.x + 0
            nextY = cell.y - 1
        if direction == 2:  # right
            nextX = cell.x + 1
            nextY = cell.y + 0
        if direction == 3:  # left
            nextX = cell.x - 1
            nextY = cell.y + 0

        self.visitedCount+1
        nextCell = singleCell()
        nextCell.set_visited_status(True)
        nextCell.set_node_coord(nextX, nextY)
        return nextCell


cells = singleCell()
genn = mazeGen(cells)

genn.depth_first_search_maze_gen()
