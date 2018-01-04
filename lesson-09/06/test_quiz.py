## IMPORTANT: You may uncomment the test cases below to test your code.
## But when you submit this code, your test cases MUST be commented
## out.
##
## You can test whether your particle filter works using the
## function check_output (see test case 2). We will be using a similar
## function. Note: Even for a well-implemented particle filter this
## function occasionally returns False. This is because a particle
## filter is a randomized algorithm. We will be testing your code
## multiple times. Make sure check_output returns True at least 80%
## of the time.

from finalquiz import particle_filter, generate_ground_truth, print_measurements, check_output
from math import *
from pytest import raises, approx

## --------
## TEST CASES:
##
##1) Calling the particle_filter function with the following
##    motions and measurements should return a [x,y,orientation]
##    vector near [x=93.476 y=75.186 orient=5.2664], that is, the
##    robot's true location.
##
def test_1():
    motions = [[2. * pi / 10, 20.] for row in range(8)]
    measurements = [[4.746936, 3.859782, 3.045217, 2.045506],
                   [3.510067, 2.916300, 2.146394, 1.598332],
                   [2.972469, 2.407489, 1.588474, 1.611094],
                   [1.906178, 1.193329, 0.619356, 0.807930],
                   [1.352825, 0.662233, 0.144927, 0.799090],
                   [0.856150, 0.214590, 5.651497, 1.062401],
                   [0.194460, 5.660382, 4.761072, 2.471682],
                   [5.717342, 4.736780, 3.909599, 2.342536]]


    # according to Sebastian about 80% of the solution should be valid ( a little vague but anyhow....)
    error_cnt = 0
    for i in range(5):
        result = particle_filter(motions, measurements)
        if result[0] != approx(93.476, rel=1e-1) or \
           result[1] != approx(75.186, rel=1e-1) or \
           result[2] != approx(5.2664, rel=1e-1):
            error_cnt += 1

    assert error_cnt <= 1

## 2) You can generate your own test cases by generating
##    measurements using the generate_ground_truth function.
##    It will print the robot's last location when calling it.
##
##
def test_2():
    number_of_iterations = 6
    motions = [[2. * pi / 20, 12.] for row in range(number_of_iterations)]

    x = generate_ground_truth(motions)
    final_robot = x[0]
    measurements = x[1]
    estimated_position = particle_filter(motions, measurements)
    print_measurements(measurements)
    print 'Ground truth:    ', final_robot
    print 'Particle filter: ', estimated_position
    result = check_output(final_robot, estimated_position)
    print 'Code check:      ', result



