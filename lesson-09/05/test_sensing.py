from sensing import robot

from math import *

from pytest import raises, approx

## IMPORTANT: You may uncomment the test cases below to test your code.
## But when you submit this code, your test cases MUST be commented
## out. Our testing program provides its own code for testing your
## sense function with randomized initial robot coordinates.

## --------
## TEST CASES:


##
## 1) The following code should print the list [6.004885648174475, 3.7295952571373605, 1.9295669970654687, 0.8519663271732721]
##
##
def test_1():
    length = 20.
    bearing_noise  = 0.0
    steering_noise = 0.0
    distance_noise = 0.0

    myrobot = robot(length)
    myrobot.set(30.0, 20.0, 0.0)
    myrobot.set_noise(bearing_noise, steering_noise, distance_noise)

    print('Robot:        ', myrobot)
    Z = myrobot.sense()
    print('Measurements: ', Z)

    expected = [6.004885648174475, 3.7295952571373605, 1.9295669970654687, 0.8519663271732721]

    for i in range(len(Z)):
        assert expected[i] == approx(Z[i], rel=1e-3)


## IMPORTANT: You may uncomment the test cases below to test your code.
## But when you submit this code, your test cases MUST be commented
## out. Our testing program provides its own code for testing your
## sense function with randomized initial robot coordinates.


##
## 2) The following code should print the list [5.376567117456516, 3.101276726419402, 1.3012484663475101, 0.22364779645531352]
##
##
def test_2():
    length = 20.
    bearing_noise  = 0.0
    steering_noise = 0.0
    distance_noise = 0.0

    myrobot = robot(length)
    myrobot.set(30.0, 20.0, pi / 5.0)
    myrobot.set_noise(bearing_noise, steering_noise, distance_noise)

    print('Robot:        ', myrobot)
    Z = myrobot.sense()
    print('Measurements: ', Z)

    expected = [5.376567117456516, 3.101276726419402, 1.3012484663475101, 0.22364779645531352]

    for i in range(len(Z)):
        assert expected[i] == approx(Z[i], rel=1e-3)

## IMPORTANT: You may uncomment the test cases below to test your code.
## But when you submit this code, your test cases MUST be commented
## out. Our testing program provides its own code for testing your
## sense function with randomized initial robot coordinates.

