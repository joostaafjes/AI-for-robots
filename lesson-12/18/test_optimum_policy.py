from optimum_policy import optimum_policy

def test_1():

    grid = [[0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0]]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1 # the cost associated with moving from a cell to an adjacent one

    policy = optimum_policy(grid, goal, cost)

    print('--------------------------------------------')
    for row in policy:
        print(row)
    print('--------------------------------------------')

    assert policy == [['v', ' ', 'v', 'v', 'v', 'v'],
                      ['v', ' ', 'v', 'v', 'v', 'v'],
                      ['v', ' ', 'v', 'v', 'v', 'v'],
                      ['v', ' ', '>', '>', '>', 'v'],
                      ['>', '>', '^', '^', ' ', '*']]

def test_2():

    grid = [[0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0]]
    goal = [len(grid) - 1, len(grid[0]) - 1]
    cost = 1  # the cost associated with moving from a cell to an adjacent one

    policy = optimum_policy(grid, goal, cost)

    print('--------------------------------------------')
    for row in policy:
        print(row)
    print('--------------------------------------------')

    assert policy == [['v', 'v', ' ', 'v', 'v', 'v'],
                      ['v', 'v', ' ', 'v', 'v', 'v'],
                      ['v', 'v', ' ', '>', '>', 'v'],
                      ['>', '>', '>', '^', ' ', 'v'],
                      ['^', '^', ' ', ' ', ' ', 'v'],
                      ['^', '^', '<', '<', ' ', '*']]

def test_fail():

    grid = [[0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0]]
    goal = [len(grid) - 1, len(grid[0]) - 1]
    cost = 1  # the cost associated with moving from a cell to an adjacent one

    policy = optimum_policy(grid, goal, cost)

    print('--------------------------------------------')
    for row in policy:
        print(row)
    print('--------------------------------------------')

    assert policy == [[' ', ' ', ' ', ' ', 'v', 'v'],
                      [' ', ' ', ' ', ' ', 'v', 'v'],
                      [' ', ' ', ' ', ' ', 'v', 'v'],
                      [' ', ' ', ' ', ' ', 'v', 'v'],
                      [' ', ' ', ' ', ' ', '>', '*']]

