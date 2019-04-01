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

        while self.visitedCount != (self.size * self.size):
            self.grid[0][0].set_node_coord(0, 0)    # starting cell is at (0, 0)
            dfsQ.put(self.grid[0][0])               # put current cell on queue

            nextCell = self.get_rand_node(self.grid[0][0])  # check adjacent cells if visited and get next rand cell
            dfsQ.put(nextCell)

        '''
        x, y = self.get_rand_node() #get random cell in self.grid
        self.grid[x][y].set_node_coord(x, y) # have the grid x,y be stored by the obj thats in that position
        print ("X: " + str(x) + "| Y: " + str(y))  # rest is code to make sure it works 
        self.grid[x][y].print_node()
        self.grid[x][y].set_visited_status(True)
        self.grid[x][y].print_node()
        '''

    #  TODO: Check if adjacent cells have been visited

    def get_rand_node(self, tempCell):

        direction = random.randint(0, 3)
        if direction == 0:  # top
            nextX = tempCell.x + 0
            nextY = tempCell.y + 1
        if direction == 1:  # bottom
            nextX = tempCell.x + 0
            nextY = tempCell.y - 1
        if direction == 2:  # right
            nextX = tempCell.x + 1
            nextY = tempCell.y + 0
        if direction == 3:  # left
            nextX = tempCell.x - 1
            nextY = tempCell.y + 0


        nextCell = singleCell()
        nextCell.set_node_coord(nextX, nextY)
        return nextCell


cells = singleCell()
genn = mazeGen(cells)

genn.depth_first_search_maze_gen()
