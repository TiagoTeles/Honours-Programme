# ========== Imports ========== #
from math import sin, cos, sqrt
from numpy import array

# ========== Function Definitions ========== #
def radius(x):
    return sqrt(x[0]**2 + x[1]**2 + x[2]**2)

def velocity(x):
    return sqrt(x[3]**2 + x[4]**2 + x[5]**2)

def norm(x):
    return sqrt(x[0]**2 + x[1]**2 + x[2]**2)

def density(x):
    return 1E-12

def rotate_x(a):
    return array([
        [1.0,    0.0,     0.0],
        [0.0, cos(a), -sin(a)],
        [0.0, sin(a),  cos(a)]])

def rotate_y(a):
    return array([
        [ cos(a), 0.0, sin(a)],
        [    0.0, 1.0,    0.0],
        [-sin(a), 0.0, cos(a)]])

def rotate_z(a):
    return array([
        [cos(a), -sin(a), 0.0],
        [sin(a),  cos(a), 0.0],
        [   0.0,     0.0, 1.0]])
