from first_search_program import search, get_list_from_node, extend_list

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

    assert search(grid, init, goal, cost) == [11, 4, 5]

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

    assert search(grid, init, goal, cost) == [9, 4, 5]

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

    assert search(grid, init, goal, cost) == [15, 4, 5]

def test_3():
    # Grid format:
    #   0 = Navigable space
    #   1 = Occupied space

    grid = [[0, 1],
            [0, 0]]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1

    assert search(grid, init, goal, cost) == [2, 1, 1]

def test_one_cell_that_fails():
    grid = [[0]]
    list = [0, 0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1

    assert get_list_from_node(list, grid, 0, 1) == []

def test_extend_1():
    assert extend_list([[0, 0, 0]], [[1, 0, 0]]) == [[0, 0, 0]]

def test_extend_2():
    assert extend_list([[0, 0, 1]], [[1, 0, 0]]) == [[0, 0, 1], [1, 0, 0]]

def test_extend_3():
    assert extend_list([[0, 0, 1], [0, 1, 0]], [[1, 0, 0], [0, 1, 0]]) == [[0, 0, 1], [0, 1, 0], [1, 0, 0]]

def test_fail_1():
    # Grid format:
    #   0 = Navigable space
    #   1 = Occupied space

    grid = [[0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 1, 1, 1, 0],
            [0, 0, 0, 0, 1, 0]]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1

    assert search(grid, init, goal, cost) == 'fail'

def test_fail_2():
    # Grid format:
    #   0 = Navigable space
    #   1 = Occupied space

    grid = [[0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 1, 1],
            [0, 0, 1, 1, 1, 0],
            [0, 0, 1, 0, 1, 0]]
    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1

    assert search(grid, init, goal, cost) == 'fail'
