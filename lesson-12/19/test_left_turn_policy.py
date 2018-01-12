from left_turn_policy import optimum_policy2D

def test_1():

    # grid format:
    #     0 = navigable space
    #     1 = unnavigable space
    grid = [[0, 0]]

    init = [0, 0, 3]  # given in the form [row,col,direction]
    # direction = 0: up
    #             1: left
    #             2: down
    #             3: right

    goal = [0, 1]  # given in the form [row,col]

    cost = [1, 1, 1]  # cost has 3 values, corresponding to making
    # a right turn, no turn, and a left turn

    policy = optimum_policy2D(grid, init, goal, cost)

    print('--------------------------------------------')
    for row in policy:
        print(row)
    print('--------------------------------------------')

    assert [['#', '*']] == policy

def test_2():

    # grid format:
    #     0 = navigable space
    #     1 = unnavigable space
    grid = [[0, 0],
            [0, 0]]

    init = [0, 0, 3]  # given in the form [row,col,direction]
                      # direction = 0: up
                      #             1: left
                      #             2: down
                      #             3: right

    goal = [1, 1]  # given in the form [row,col]

    cost = [1, 1, 2]  # cost has 3 values, corresponding to making
                       # a right turn, no turn, and a left turn

    policy = optimum_policy2D(grid, init, goal, cost)

    print('--------------------------------------------')
    for row in policy:
        print(row)
    print('--------------------------------------------')

    assert [['#', 'R'],
            [' ', '*']] == policy

def test_3():

    # grid format:
    #     0 = navigable space
    #     1 = unnavigable space
    grid = [[1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0],
            [1, 1, 1, 0, 1, 1],
            [1, 1, 1, 0, 1, 1]]

    init = [4, 3, 0]  # given in the form [row,col,direction]
    # direction = 0: up
    #             1: left
    #             2: down
    #             3: right

    goal = [2, 0]  # given in the form [row,col]

    cost = [2, 1, 20]  # cost has 3 values, corresponding to making
    # a right turn, no turn, and a left turn

    policy = optimum_policy2D(grid, init, goal, cost)

    print('--------------------------------------------')
    for row in policy:
        print(row)
    print('--------------------------------------------')

    assert [[' ', ' ', ' ', 'R', '#', 'R'],
            [' ', ' ', ' ', '#', ' ', '#'],
            ['*', '#', '#', '#', '#', 'R'],
            [' ', ' ', ' ', '#', ' ', ' '],
            [' ', ' ', ' ', '#', ' ', ' ']] == policy

def test_4():
    grid = [[0, 0, 0, 0, 1, 1],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0]]
    init = [4, 5, 0]
    goal = [4, 3]
    cost = [1, 1, 1]

    policy = optimum_policy2D(grid, init, goal, cost)

    print('--------------------------------------------')
    for row in policy:
        print(row)
    print('--------------------------------------------')

    assert [[' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', 'L', '#', 'L'],
            [' ', 'L', '#', 'R', ' ', '#'],
            [' ', '#', ' ', ' ', ' ', '#'],
            [' ', 'L', '#', '*', ' ', '#']] == policy
