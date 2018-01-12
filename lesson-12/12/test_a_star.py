from a_star import search

def test_1():
    # Grid format:
    #   0 = Navigable space
    #   1 = Occupied space

    grid = [[0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0]]

    heuristic = [[9, 8, 7, 6, 5, 4],
                 [8, 7, 6, 5, 4, 3],
                 [7, 6, 5, 4, 3, 2],
                 [6, 5, 4, 3, 2, 1],
                 [5, 4, 3, 2, 1, 0]]

    init = [0, 0]
    goal = [len(grid)-1, len(grid[0])-1]
    cost = 1

    expand = search(grid, init, goal, cost, heuristic)

    print('--------------------------------------------')
    for row in expand:
        print(row)
    print('--------------------------------------------')

    assert expand == [[0, -1, -1, -1, -1, -1],
                      [1, -1, -1, -1, -1, -1],
                      [2, -1, -1, -1, -1, -1],
                      [3, -1, 8, 9, 10, 11],
                      [4, 5, 6, 7, -1 , 12]]


