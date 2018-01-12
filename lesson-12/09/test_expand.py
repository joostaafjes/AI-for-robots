from expansion_grid import search

def test_1():
    # Grid format:
    #   0 = Navigable space
    #   1 = Occupied space

    grid = [[0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0]]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1

    print search(grid, init, goal, cost)

def test_2():
    # Grid format:
    #   0 = Navigable space
    #   1 = Occupied space

    grid = [[0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0]]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1

    print(search(grid, init, goal, cost))

def test_3():
    # Grid format:
    #   0 = Navigable space
    #   1 = Occupied space

    grid = [[0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 1, 0]]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1

    print(search(grid, init, goal, cost))

def test_4():
    # Grid format:
    #   0 = Navigable space
    #   1 = Occupied space

    grid = [[0, 1],
            [0, 0]]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1

    print(search(grid, init, goal, cost))

def test_5():
    # Grid format:
    #   0 = Navigable space
    #   1 = Occupied space

    grid = [[0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0]]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1

    print(search(grid, init, goal, cost))

def test_6():
    # Grid format:
    #   0 = Navigable space
    #   1 = Occupied space

    grid = [[0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0],
            [0, 0, 1, 0, 1, 0]]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1

    print('-------------------------------------')
    expand = search(grid, init, goal, cost)

    for row in expand:
        print(row)

def test_7():
    # Grid format:
    #   0 = Navigable space
    #   1 = Occupied space

    grid = [[0, 1, 1, 1, 1],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 1, 1, 0],
            [0, 0, 0, 1, 0]]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1

    print('-------------------------------------')
    expand = search(grid, init, goal, cost)

    for row in expand:
        print(row)
