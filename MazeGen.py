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


#  enum for sides, used for self.walls
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
        #  for (wallPresent, side) in zip(self.walls, sides):
        #    print( str(side.name) + " side: " + str(wallPresent))
    
    def set_visited_status(self, visited): 
        #  print("Changed visited status to visited")
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
        dfs_stack = []
        i = 0
        j = 0
        start_cell = singleCell()
        start_cell.set_node_coord(0, 0)
        start_cell.set_visited_status(True)
        self.grid[0][0] = start_cell
        dfs_stack.append(self.grid[0][0])       # put first cell in stack
        while self.visitedCount != (25):
            #  if bool = true, then pop queue
            print(self.all_adjacent_visited(self.grid[i][j]))
            if self.all_adjacent_visited(self.grid[i][j]):
                dfs_stack.pop()
                next_cell = dfs_stack.pop()
            if not self.all_adjacent_visited(self.grid[i][j]):
                next_cell = self.get_rand_node(self.grid[i][j])  # get next rand cell, given current cell
            i = next_cell.x
            j = next_cell.y
            self.grid[i][j] = next_cell
            dfs_stack.append(next_cell)
            #  next_cell.print_node()

    #  TODO: Do not allow visited nodes to be selected
    #  Ex. If bottom is visited, find a way so that 1 (bottom) cant be randomly selected
    def get_rand_node(self, cell):
        self.visitedCount += 1
        direction = random.randint(0, 3)
        next_x = cell.x + 0
        next_y = cell.y + 0
        if direction == 0 and cell.x != 0:  # top
            next_x = cell.x - 1
            next_y = cell.y + 0
        if direction == 1 and cell.x != (self.size - 1):  # bottom
            next_x = cell.x + 1
            next_y = cell.y + 0
        if direction == 2 and cell.y != (self.size - 1):  # right
            next_x = cell.x + 0
            next_y = cell.y + 1
        if direction == 3 and cell.y != 0:  # left
            next_x = cell.x + 0
            next_y = cell.y - 1
        temp_cell = singleCell()
        temp_cell.set_visited_status(True)
        temp_cell.set_node_coord(next_x, next_y)
        return temp_cell

    def all_adjacent_visited(self, node):
        x = node.x
        y = node.y
        if x != 0:
            if not self.grid[x - 1][y].get_visited_status():  # check top
                return False
        if x != self.size - 1:
            if not self.grid[x + 1][y].get_visited_status():  # check bottom
                return False
        if y != 0:
            if not self.grid[x][y - 1].get_visited_status():  # check left
                return False
        if y != self.size - 1:
            if not self.grid[x][y + 1].get_visited_status():  # check right
                return False
        return True

def print_grid(grid):
    for row in grid:
        for e in row:
            if e.get_visited_status():
                print("V", end=' ')  # Visited
            else:
                print("N", end=' ')  # Not Visited

        print('\n')


cells = singleCell()
genn = mazeGen(cells)

genn.depth_first_search_maze_gen()
print_grid(genn.grid)
