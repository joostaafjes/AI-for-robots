# -----------------
# USER INSTRUCTIONS
#
# Write a function in the class robot called move()
#
# that takes self and a motion vector (this
# motion vector contains a steering* angle and a
# distance) as input and returns an instance of the class
# robot with the appropriate x, y, and orientation
# for the given motion.
#
# *steering is defined in the video
# which accompanies this problem.
#
# For now, please do NOT add noise to your move function.
#
# Please do not modify anything except where indicated
# below.
#
# There are test cases which you are free to use at the
# bottom. If you uncomment them for testing, make sure you
# re-comment them before you submit.

from math import *
import random

# --------
#
# the "world" has 4 landmarks.
# the robot's initial coordinates are somewhere in the square
# represented by the landmarks.
#
# NOTE: Landmark coordinates are given in (y, x) form and NOT
# in the traditional (x, y) format!

landmarks = [[0.0, 100.0], [0.0, 0.0], [100.0, 0.0], [100.0, 100.0]]  # position of 4 landmarks
world_size = 100.0  # world is NOT cyclic. Robot is allowed to travel "out of bounds"
max_steering_angle = pi / 4  # You don't need to use this value, but it is good to keep in mind the limitations of a real car.


# ------------------------------------------------
#
# this is the robot class
#

class robot:

    # --------

    # init:
    #	creates robot and initializes location/orientation
    #

    def __init__(self, length=10.0):
        self.x = random.random() * world_size  # initial x position
        self.y = random.random() * world_size  # initial y position
        self.orientation = random.random() * 2.0 * pi  # initial orientation
        self.length = length  # length of robot
        self.bearing_noise = 0.0  # initialize bearing noise to zero
        self.steering_noise = 0.0  # initialize steering noise to zero
        self.distance_noise = 0.0  # initialize distance noise to zero

    def __repr__(self):
        return '[x=%.6s y=%.6s orient=%.6s]' % (str(self.x), str(self.y), str(self.orientation))

    # --------
    # set:
    #	sets a robot coordinate
    #

    def set(self, new_x, new_y, new_orientation):
        if new_orientation < 0 or new_orientation >= 2 * pi:
            raise ValueError('Orientation must be in [0..2pi]')
        self.x = float(new_x)
        self.y = float(new_y)
        self.orientation = float(new_orientation)

    # --------
    # set_noise:
    #	sets the noise parameters
    #

    def set_noise(self, new_b_noise, new_s_noise, new_d_noise):
        # makes it possible to change the noise parameters
        # this is often useful in particle filters
        self.bearing_noise = float(new_b_noise)
        self.steering_noise = float(new_s_noise)
        self.distance_noise = float(new_d_noise)

    ############# ONLY ADD/MODIFY CODE BELOW HERE ###################

    # --------
    # move:
    #   move along a section of a circular path according to motion
    #

    def move(self, motion):  # Do not change the name of this function

        # ADD CODE HERE
        steering_angle = motion[0]
        distance = motion[1]

        if abs(steering_angle) > max_steering_angle:
            raise ValueError('Max steering angle exceeded')

        if distance < 0:
            raise ValueError('Cannot move backwards')

        turning_angle = distance / self.length * tan(steering_angle)

        if turning_angle >= 0.001:
            radius = distance / turning_angle
            cx = self.x - radius * sin(self.orientation)
            cy = self.y + radius * cos(self.orientation)
            self.x = cx + radius * sin(self.orientation + turning_angle)
            self.y = cy - radius * cos(self.orientation + turning_angle)
            self.orientation = (self.orientation + turning_angle) % (2 * pi)
        else:
            self.x += distance * cos(self.orientation)
            self.y += distance * sin(self.orientation)
            self.orientation = (self.orientation + turning_angle) % (2 * pi)

        return self
        # make sure your move function returns an instance
        # of the robot class with the correct coordinates.

    ############## ONLY ADD/MODIFY CODE ABOVE HERE ####################


