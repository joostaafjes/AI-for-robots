## IMPORTANT: You may uncomment the test cases below to test your code.
## But when you submit this code, your test cases MUST be commented
## out. Our testing program provides its own code for testing your
## move function with randomized motion data.

from circulairmotion import *
from math import *
import copy

from pytest import raises, approx

## --------
## TEST CASE:
##
##
##
def test_1():
    length = 20.
    bearing_noise  = 0.0
    steering_noise = 0.0
    distance_noise = 0.0

    myrobot = robot(length)
    myrobot.set(0.0, 0.0, 0.0)
    myrobot.set_noise(bearing_noise, steering_noise, distance_noise)

    motions = [[0.0, 10.0], [pi / 6.0, 10], [0.0, 20.0]]

    T = len(motions)

    history = []
    history.append(copy.deepcopy(myrobot))
    print('Robot:    ', myrobot)
    for t in range(T):
       myrobot = myrobot.move(motions[t])
       history.append(copy.deepcopy(myrobot))
       print('Robot:    ', myrobot)

    correct_answer = (
      [[0.0, 0.0, 0.0],
      [10.0, 0.0, 0.0],
      [19.861, 1.4333, 0.2886],
      [39.034, 7.1270, 0.2886]])

    for row_index, row in enumerate(history):
        assert history[row_index].x == approx(correct_answer[row_index][0], rel=1e-3)
        assert history[row_index].y == approx(correct_answer[row_index][1], rel=1e-3)
        assert history[row_index].orientation == approx(correct_answer[row_index][2], rel=1e-3)

## IMPORTANT: You may uncomment the test cases below to test your code.
## But when you submit this code, your test cases MUST be commented
## out. Our testing program provides its own code for testing your
## move function with randomized motion data.


## 2) The following code should print:
##
##
def test_2():
    length = 20.
    bearing_noise  = 0.0
    steering_noise = 0.0
    distance_noise = 0.0

    myrobot = robot(length)
    myrobot.set(0.0, 0.0, 0.0)
    myrobot.set_noise(bearing_noise, steering_noise, distance_noise)

    motions = [[0.2, 10.] for row in range(10)]

    T = len(motions)

    print('Robot:    ', myrobot)
    history = []
    history.append(copy.deepcopy(myrobot))
    for t in range(T):
       myrobot = myrobot.move(motions[t])
       history.append(copy.deepcopy(myrobot))
       print('Robot:    ', myrobot)

    correct_answer = (
         [[0.0, 0.0, 0.0],
         [9.9828, 0.5063, 0.1013],
         [19.863, 2.0201, 0.2027],
         [29.539, 4.5259, 0.3040],
         [38.913, 7.9979, 0.4054],
         [47.887, 12.400, 0.5067],
         [56.369, 17.688, 0.6081],
         [64.273, 23.807, 0.7094],
         [71.517, 30.695, 0.8108],
         [78.027, 38.280, 0.9121],
         [83.736, 46.485, 1.0135]])

    for row_index, row in enumerate(history):
        assert history[row_index].x == approx(correct_answer[row_index][0], rel=1e-3)
        assert history[row_index].y == approx(correct_answer[row_index][1], rel=1e-3)
        assert history[row_index].orientation == approx(correct_answer[row_index][2], rel=1e-3)

## IMPORTANT: You may uncomment the test cases below to test your code.
## But when you submit this code, your test cases MUST be commented
## out. Our testing program provides its own code for testing your
## move function with randomized motion data.


