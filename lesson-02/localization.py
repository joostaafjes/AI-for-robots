# The function localize takes the following arguments:
#
# colors:
#        2D list, each entry either 'R' (for red cell) or 'G' (for green cell)
#
# measurements:
#        list of measurements taken by the robot, each entry either 'R' or 'G'
#
# motions:
#        list of actions taken by the robot, each entry of the form [dy,dx],
#        where dx refers to the change in the x-direction (positive meaning
#        movement to the right) and dy refers to the change in the y-direction
#        (positive meaning movement downward)
#        NOTE: the *first* coordinate is change in y; the *second* coordinate is
#              change in x
#
# sensor_right:
#        float between 0 and 1, giving the probability that any given
#        measurement is correct; the probability that the measurement is
#        incorrect is 1-sensor_right
#
# p_move:
#        float between 0 and 1, giving the probability that any given movement
#        command takes place; the probability that the movement command fails
#        (and the robot remains still) is 1-p_move; the robot will NOT overshoot
#        its destination in this exercise
#
# The function should RETURN (not just show or print) a 2D list (of the same
# dimensions as colors) that gives the probabilities that the robot occupies
# each cell in the world.
#
# Compute the probabilities by assuming the robot initially has a uniform
# probability of being in any cell.
#
# Also assume that at each step, the robot:
# 1) first makes a movement,
# 2) then takes a measurement.
#
# Motion:
#  [0,0] - stay
#  [0,1] - right
#  [0,-1] - left
#  [1,0] - down
#  [-1,0] - up
import sys


def localize(colors, measurements, motions, sensor_right, p_move):
    # initializes p to a uniform distribution over a grid of the same dimensions as colors
    pinit = 1.0 / float(len(colors)) / float(len(colors[0]))
    p = [[pinit for row in range(len(colors[0]))] for col in range(len(colors))]

    if len(measurements) != len(motions):
        sys.exit('# of measurement(%s) not the same as motions(%s) '.format(len(measurements), len(motions)))

    for count in range(len(measurements)):
        p = move(p, motions[count], p_move)
        p = sense(p, measurements[count], colors, sensor_right)

    return p

def sense(p, measurement, colors, p_sensor_right):
    q = []
    for row_index, row in enumerate(p):
        new_row = []
        for column_index, column in enumerate(row):
           hit = (measurement == colors[row_index][column_index])
           new_row.append(p[row_index][column_index] * (hit * p_sensor_right + (1-hit) * (1 - p_sensor_right)))
        q.append(new_row)

    return normalize(q)

def normalize(matrix):
    s = 0
    for row_index, row in enumerate(matrix):
        s = s + sum(matrix[row_index])
    norm_matrix=[]
    for row_index, row in enumerate(matrix):
        new_row=[]
        for column_index, column in enumerate(row):
            new_row.append(matrix[row_index][column_index] / s)
        norm_matrix.append(new_row)

    return norm_matrix

def move(p, motion, p_move):
    q = []
    for row_index, row in enumerate(p):
        new_row = []
        for column_index, column in enumerate(row):
            new_row.append(p_move * p[(row_index - motion[0]) % len(p)][(column_index - motion[1]) % len(row)] +
                           (1 - p_move) * p[row_index][column_index])
        q.append(new_row)

    return q


def show(p):
    rows = ['[' + ','.join(map(lambda x: '{0:.5f}'.format(x), r)) + ']' for r in p]
    print('[' + ',\n '.join(rows) + ']')

