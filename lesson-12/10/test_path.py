from print_path import search

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

    print('--------------------------------------------')
    expand = search(grid, init, goal, cost)

    assert expand == [['v', ' ', ' ', ' ', ' ', ' '],
                      ['v', ' ', ' ', '>', '>', 'v'],
                      ['>', '>', '>', '^', ' ', 'v'],
                      [' ', ' ', ' ', ' ', ' ', 'v'],
                      [' ', ' ', ' ', ' ', ' ', '*']]

    for row in expand:
        print row
    print('--------------------------------------------')

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

    print('--------------------------------------------')
    expand = search(grid, init, goal, cost)
    assert expand == [['v', ' ', ' ', ' ', ' ', ' '],
                      ['>', '>', '>', '>', '>', 'v'],
                      [' ', ' ', ' ', ' ', ' ', 'v'],
                      [' ', ' ', ' ', ' ', ' ', 'v'],
                      [' ', ' ', ' ', ' ', ' ', '*']]
    for row in expand:
        print row
    print('--------------------------------------------')

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

    print('--------------------------------------------')
    expand = search(grid, init, goal, cost)
    assert expand == [['v', ' ', ' ', ' ', ' ', ' '],
                      ['v', ' ', ' ', '>', '>', 'v'],
                      ['v', ' ', ' ', '^', ' ', 'v'],
                      ['v', ' ', ' ', '^', ' ', 'v'],
                      ['>', '>', '>', '^', ' ', '*']]
    for row in expand:
        print row
    print('--------------------------------------------')

def test_4():
    # Grid format:
    #   0 = Navigable space
    #   1 = Occupied space

    grid = [[0, 1],
            [0, 0]]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1

    print('--------------------------------------------')
    expand = search(grid, init, goal, cost)
    assert expand == [['v', ' '],
                      ['>', '*']]
    for row in expand:
        print row
    print('--------------------------------------------')

def test_5():
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

    print('--------------------------------------------')
    expand = search(grid, init, goal, cost)
    assert expand == [['v', ' ', ' ', ' ', ' ', ' '],
                      ['>', '>', '>', '>', '>', 'v'],
                      [' ', ' ', ' ', ' ', ' ', 'v'],
                      [' ', ' ', ' ', ' ', ' ', 'v'],
                      [' ', ' ', ' ', ' ', ' ', '*']]
    for row in expand:
        print row
    print('--------------------------------------------')
