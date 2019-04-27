def genNode(grid, size):
    for i in range(size):
        for j in range(size):
            # Check if path can only go up or down
            if grid[j][i].walls[1] == False and grid[j][i].walls[0] == False:
                if grid[j][i].walls[2] == True and grid[j][i].walls[3] == True:
                    grid[j][i].isNode = False

            # Check if path can only go left or right
            if grid[j][i].walls[1] == True and grid[j][i].walls[0] == True:
                if grid[j][i].walls[2] == False and grid[j][i].walls[3] == False:
                    grid[j][i].isNode = False


def print_IfNodes(grid):
    for row in grid:
        for e in row:
            print(e.isNode)

