from pytest import raises, approx

from localization import localize, show

def test_expect_whenMeasurementsNotEqualToMotions():
    with raises(SystemExit):
        # test 1
        colors = [['G', 'G', 'G'],
                  ['G', 'R', 'G'],
                  ['G', 'G', 'G']]
        measurements = ['R', 'G']
        motions = [[0,0]]
        sensor_right = 1.0
        p_move = 1.0
        localize(colors,measurements,motions,sensor_right,p_move)


def test_0():
    #############################################################
    # For the following test case, your output should be
    # [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
    #  [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
    #  [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
    #  [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]
    # (within a tolerance of +/- 0.001 for each entry)

    colors = [['R', 'G', 'G', 'R', 'R'],
              ['R', 'R', 'G', 'R', 'R'],
              ['R', 'R', 'G', 'G', 'R'],
              ['R', 'R', 'R', 'R', 'R']]
    measurements = ['G', 'G', 'G', 'G', 'G']
    motions = [[0, 0], [0, 1], [1, 0], [1, 0], [0, 1]]
    p = localize(colors, measurements, motions, sensor_right=0.7, p_move=0.8)

    correct_answer = [[0.01105, 0.02464, 0.06799, 0.04472, 0.02465],
     [0.00715, 0.01017, 0.08696, 0.07988, 0.00935],
     [0.00739, 0.00894, 0.11272, 0.35350, 0.04065],
     [0.00910, 0.00715, 0.01434, 0.04313, 0.03642]]

    for row_index, row in enumerate(p):
        for column_index, column in enumerate(row):
            assert p[row_index][column_index] == approx(correct_answer[row_index][column_index], rel=1e-3)

def test_1():
    # test 1
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'G'],
              ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0,0]]
    sensor_right = 1.0
    p_move = 1.0
    p = localize(colors,measurements,motions,sensor_right,p_move)
    correct_answer = (
        [[0.0, 0.0, 0.0],
         [0.0, 1.0, 0.0],
         [0.0, 0.0, 0.0]])

    for row_index, row in enumerate(p):
        for column_index, column in enumerate(row):
            assert p[row_index][column_index] == approx(correct_answer[row_index][column_index])

def test_2():
    # test 2
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0,0]]
    sensor_right = 1.0
    p_move = 1.0
    p = localize(colors,measurements,motions,sensor_right,p_move)
    correct_answer = (
        [[0.0, 0.0, 0.0],
         [0.0, 0.5, 0.5],
         [0.0, 0.0, 0.0]])

    for row_index, row in enumerate(p):
        for column_index, column in enumerate(row):
            assert p[row_index][column_index] == approx(correct_answer[row_index][column_index])

def test_3():
    # test 3
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R']
    motions = [[0,0]]
    sensor_right = 0.8
    p_move = 1.0
    p = localize(colors,measurements,motions,sensor_right,p_move)
    correct_answer = (
        [[0.06666666666, 0.06666666666, 0.06666666666],
         [0.06666666666, 0.26666666666, 0.26666666666],
         [0.06666666666, 0.06666666666, 0.06666666666]])

    for row_index, row in enumerate(p):
        for column_index, column in enumerate(row):
            assert p[row_index][column_index] == approx(correct_answer[row_index][column_index])

def test_4():
    # test 4
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0,0], [0,1]]
    sensor_right = 0.8
    p_move = 1.0
    p = localize(colors,measurements,motions,sensor_right,p_move)
    correct_answer = (
        [[0.03333333333, 0.03333333333, 0.03333333333],
         [0.13333333333, 0.13333333333, 0.53333333333],
         [0.03333333333, 0.03333333333, 0.03333333333]])

    for row_index, row in enumerate(p):
        for column_index, column in enumerate(row):
            assert p[row_index][column_index] == approx(correct_answer[row_index][column_index])

def test_5():
    # test 5
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0,0], [0,1]]
    sensor_right = 1.0
    p_move = 1.0
    p = localize(colors,measurements,motions,sensor_right,p_move)
    correct_answer = (
        [[0.0, 0.0, 0.0],
         [0.0, 0.0, 1.0],
         [0.0, 0.0, 0.0]])

    for row_index, row in enumerate(p):
        for column_index, column in enumerate(row):
            assert p[row_index][column_index] == approx(correct_answer[row_index][column_index])

def test_6():
    # test 6
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0,0], [0,1]]
    sensor_right = 0.8
    p_move = 0.5
    p = localize(colors,measurements,motions,sensor_right,p_move)
    correct_answer = (
        [[0.0289855072, 0.0289855072, 0.0289855072],
         [0.0724637681, 0.2898550724, 0.4637681159],
         [0.0289855072, 0.0289855072, 0.0289855072]])

    for row_index, row in enumerate(p):
        for column_index, column in enumerate(row):
            assert p[row_index][column_index] == approx(correct_answer[row_index][column_index])

def test_7():
    # test 7
    colors = [['G', 'G', 'G'],
              ['G', 'R', 'R'],
              ['G', 'G', 'G']]
    measurements = ['R', 'R']
    motions = [[0,0], [0,1]]
    sensor_right = 1.0
    p_move = 0.5
    p = localize(colors,measurements,motions,sensor_right,p_move)
    correct_answer = (
        [[0.0, 0.0, 0.0],
         [0.0, 0.33333333, 0.66666666],
         [0.0, 0.0, 0.0]])

    for row_index, row in enumerate(p):
        for column_index, column in enumerate(row):
            assert p[row_index][column_index] == approx(correct_answer[row_index][column_index])

