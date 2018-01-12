from value_program import compute_value

def test_1():

    grid = [[0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0]]
    goal = [len(grid) - 1, len(grid[0]) - 1]
    cost = 1  # the cost associated with moving from a cell to an adjacent one

    value = compute_value(grid, goal, cost)

    print('--------------------------------------------')
    for row in value:
        print(row)
    print('--------------------------------------------')

    assert value == [[11, 99, 7, 6, 5, 4],
                    [10, 99, 6, 5, 4, 3],
                    [9, 99, 5, 4, 3, 2],
                    [8, 99, 4, 3, 2, 1],
                    [7, 6, 5, 4, 99, 0]]

def test_2():

    grid = [[0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0]]
    goal = [len(grid) - 1, len(grid[0]) - 1]
    cost = 1  # the cost associated with moving from a cell to an adjacent one

    value = compute_value(grid, goal, cost)

    print('--------------------------------------------')
    for row in value:
        print(row)
    print('--------------------------------------------')

    assert value == [[12, 11, 99, 7, 6, 5],
            [11, 10, 99, 6, 5, 4],
            [10, 9, 99, 5, 4, 3],
            [9, 8, 7, 6, 99, 2],
            [10, 9, 99, 99, 99, 1],
            [11, 10, 11, 12, 99, 0]]

def test_fail():

    grid = [[0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0]]
    goal = [len(grid) - 1, len(grid[0]) - 1]
    cost = 1  # the cost associated with moving from a cell to an adjacent one

    value = compute_value(grid, goal, cost)

    print('--------------------------------------------')
    for row in value:
        print(row)
    print('--------------------------------------------')

    assert value == [[99, 99, 99, 99, 5, 4],
                     [99, 99, 99, 99, 4, 3],
                     [99, 99, 99, 99, 3, 2],
                     [99, 99, 99, 99, 2, 1],
                     [99, 99, 99, 99, 1, 0]]
