import enum
import random


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
    def __init__(self, cellObj):
        self.mazeSize = 6
        self.grid = [[cellObj for x in range(self.mazeSize)] for y in range(self.mazeSize)]  # n by m matrix
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
        while self.visitedCount != (self.mazeSize * self.mazeSize) - 1:  # Loop until all cells are visited
            #  if all adjacent nodes are visited, backtrack by popping
            if self.all_adjacent_visited(self.grid[i][j]):
                dfs_stack.pop()
                next_cell = dfs_stack.pop()
            else:
                next_cell = self.get_rand_node(self.grid[i][j])  # get next random cell, given current cell

            i = next_cell.x
            j = next_cell.y
            self.grid[i][j] = next_cell
            dfs_stack.append(next_cell)  # Add the next cell to the stack
            # print_grid(genn.grid)
            # print("-----------------------")

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
        if sideList[direction] == sides.top and cell.x != 0:  # top
            next_x = cell.x - 1
            next_y = cell.y + 0
            # print ("TOP: (" + str(next_x) + "," + str(next_y) + ")")
        if sideList[direction] == sides.bottom and cell.x != (self.mazeSize - 1):  # bottom
            next_x = cell.x + 1
            next_y = cell.y + 0
            # print ("BOT:(" + str(next_x) + "," + str(next_y) + ")")
        if sideList[direction] == sides.right and cell.y != (self.mazeSize - 1):  # right
            next_x = cell.x + 0
            next_y = cell.y + 1
            # print ("RIGHT (" + str(next_x) + "," + str(next_y) + ")")
        if sideList[direction] == sides.left and cell.y != 0:  # left
            next_x = cell.x + 0
            next_y = cell.y - 1
            # print ("LEFT: (" + str(next_x) + "," + str(next_y) + ")")
        temp_cell = singleCell()
        temp_cell.set_visited_status(True)
        temp_cell.set_node_coord(next_x, next_y)


        return temp_cell

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


cells = singleCell()
genn = mazeGen(cells)

genn.depth_first_search_maze_gen()

print_grid(genn.grid)
