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

def genNeighbor(grid, size):
    # up 0, down 1, right 2, left 3
    for i in range(size):
        for j in range(size):
            if grid[j][i].isNode:
                if grid[j][i].walls[0] == False:
                    k = j - 1
                    while not grid[k][i].isNode:
                        k -= 1
                    grid[j][i].neighbors["Top"] = grid[k][i]

                if grid[j][i].walls[1] == False:
                    k = j + 1
                    while not grid[k][i].isNode:
                        k += 1
                    grid[j][i].neighbors["Bottom"] = grid[k][i]

                # if right is false, find nearest neighbor
                if grid[j][i].walls[2] == False:
                    k = i + 1
                    while not grid[j][k].isNode:
                        k += 1
                    grid[j][i].neighbors["Right"] = grid[j][k]

                if grid[j][i].walls[3] == False:
                    k = i - 1
                    while not grid[j][k].isNode:
                        k -= 1
                    grid[j][i].neighbors["Left"] = grid[j][k]

def print_Neighbors(grid, direction):
    for row in grid:
        for e in row:
            if direction == 0:
                if e.neighbors["Top"] != None:
                    print("Node at: (", e.x, e.y, ")", "Top neighbor is:", end=" ")
                    e.neighbors["Top"].print_node()
            if direction == 1:
                if e.neighbors["Bottom"] != None:
                    print("Node at: (", e.x, e.y, ")", "Bottom neighbor is:", end=" ")
                    e.neighbors["Bottom"].print_node()
            if direction == 2:
                if e.neighbors["Right"] != None:
                    print("Node at: (", e.x, e.y, ")", "Right neighbor is:", end =" ")
                    e.neighbors["Right"].print_node()
            if direction == 3:
                if e.neighbors["Left"] != None:
                    print("Node at: (", e.x, e.y, ")", "Left neighbor is:", end=" ")
                    e.neighbors["Left"].print_node()


