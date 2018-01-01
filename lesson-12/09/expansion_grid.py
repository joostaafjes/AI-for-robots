# ----------
# User Instructions:
#
# Define a function, search() that returns a list
# in the form of [optimal path length, row, col]. For
# the grid shown below, your function should output
# [11, 4, 5].
#
# If there is no valid path from the start point
# to the goal, your function should return the string
# 'fail'
# ----------
import logging

logging.basicConfig(level=logging.INFO)

delta = [[-1, 0], # go up
         [ 0,-1], # go left
         [ 1, 0], # go down
         [ 0, 1]] # go right

delta_name = ['^', '<', 'v', '>']

def search(grid, init, goal, cost):
    # search in grid until goal is reached
    g = 0
    list = []
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]
    increment = 0
    expand[init[0]][init[1]] = increment
    list.append([g, init[0], init[1]])
    while len(list) > 0 and not(list[0][1] == goal[0] and list[0][2] == goal[1]):
        new_list = []
        for count in range(len(list)):
            current_node = list[count]
            [ext_list, expand, increment] = get_list_from_node(current_node, grid, current_node[0], cost, expand, increment)
            new_list = extend_list(new_list, ext_list)
        list = new_list
        # logging.info('new open list')
        # logging.info(list)
        # logging.info('----')

    return expand

def get_list_from_node(current_node, grid, g, cost, expand, increment):
    # search all options for 1 node and return list of found nodes
    new_list = []
    y = current_node[1]
    x = current_node[2]
    # logging.info('take list item')
    # logging.info(current_node)
    for step in range(len(delta)):
        new_y = y + delta[step][0]
        new_x = x + delta[step][1]
        if new_y < 0 or new_y > (len(grid) - 1) or \
                new_x < 0 or new_x > (len(grid[0]) - 1):
            continue
        if grid[new_y][new_x] == 1:
            continue
        increment += 1
        expand[new_y][new_x] = increment
        new_list.append([g + cost, new_y, new_x])
    grid[y][x] = 1

    return new_list, expand, increment

def extend_list(list, extend_list):
    # if node already exists with x and y, take the one with the lowest g value
    if len(list) == 0:
        list = extend_list
    else:
        for new_node in extend_list:
            found = False
            for count in range(len(list)):
                if list[count][1] == new_node[1] and list[count][2] == new_node[2]:
                    list[count][0] = min(list[count][0], new_node[0])
                    found = True
                    continue
            if not found:
                list.append(new_node)

    return list
