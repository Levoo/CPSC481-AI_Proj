def genNode(grid, size, nodes, pop_no):
    for i in range(size):
        for j in range(size):
            if ((grid[j][i].walls[1] == False and grid[j][i].walls[0] == False) and
               (grid[j][i].walls[2] == True and grid[j][i].walls[3] == True)) or \
               ((grid[j][i].walls[1] == True and grid[j][i].walls[0] == True) and
               (grid[j][i].walls[2] == False and grid[j][i].walls[3] == False)):
                    grid[j][i].isNode = False
            else:
                nodes.append(grid[j][i])
                grid[j][i].beenVisited = [(False, None) for x in range(pop_no)]
                grid[j][i].check_out = [{"up": False, "down": False, "left": False, "right": False} for x in range(pop_no)]



def genNeighbor(grid, size):
    # up 0, down 1, right 2, left 3
    for i in range(size):
        for j in range(size):
            if grid[j][i].isNode:
                if grid[j][i].walls[0] == False:
                    k = j - 1
                    while not grid[k][i].isNode:
                        k -= 1
                    grid[j][i].neighbors["up"] = grid[k][i]

                if grid[j][i].walls[1] == False:
                    k = j + 1
                    while not grid[k][i].isNode:
                        k += 1
                    grid[j][i].neighbors["down"] = grid[k][i]

                # if right is false, find nearest neighbor
                if grid[j][i].walls[2] == False:
                    k = i + 1
                    while not grid[j][k].isNode:
                        k += 1
                    grid[j][i].neighbors["right"] = grid[j][k]

                if grid[j][i].walls[3] == False:
                    k = i - 1
                    while not grid[j][k].isNode:
                        k -= 1
                    grid[j][i].neighbors["left"] = grid[j][k]


def print_Neighbors(grid, direction):
    for row in grid:
        for e in row:
            if direction == 0:
                if e.neighbors["up"] != None:
                    print("Node at: (", e.x, e.y, ")", "Top neighbor is:", end=" ")
                    e.neighbors["up"].print_node()
            if direction == 1:
                if e.neighbors["down"] != None:
                    print("Node at: (", e.x, e.y, ")", "Bottom neighbor is:", end=" ")
                    e.neighbors["down"].print_node()
            if direction == 2:
                if e.neighbors["right"] != None:
                    print("Node at: (", e.x, e.y, ")", "Right neighbor is:", end =" ")
                    e.neighbors["right"].print_node()
            if direction == 3:
                if e.neighbors["left"] != None:
                    print("Node at: (", e.x, e.y, ")", "Left neighbor is:", end=" ")
                    e.neighbors["left"].print_node()


