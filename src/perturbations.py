# ========== Imports ========== #
from numpy import array, dot
from util import norm, radius, velocity, density


# ========== Constants ========== #
R_E = 6371E3            # Radius of the Earth, [m]
MU = 3.986004418E14     # Standart gravitational parameter, [m^3/s^2]
J2 = 1.0826267E-3       # J2 Parameter, [-]


# ========== Function Definitions ========== #
def acc(x):
    return acc_central(x) + acc_srp(x) + acc_j2(x) + acc_drag(x)


def acc_central(x):
    return (-MU/radius(x)**3)*x[0:3]


def acc_j2(x):
    r = radius(x)
    C = MU*J2*R_E**2/(2*r**5)

    # Accelerations
    acc_x = C * (15*(x[2]/r)**2 - 3) * x[0]
    acc_y = C * (15*(x[2]/r)**2 - 3) * x[1]
    acc_z = C * (15*(x[2]/r)**2 - 9) * x[2]

    return array([acc_x, acc_y, acc_z])


def acc_drag(x):
    return -1.0*(0.5*density(x)*velocity(x))*(0.01/0.0276)*x[3:6]


def acc_srp(x):
    s_vec = array([1.0, 0.0, 0.0])
    vec = x[0:3] - s_vec*dot(x[0:3], s_vec)

    if norm(vec) < R_E and dot(x[0:3], s_vec) < 0.0:
        return array([-0.001, 0.0, 0.0])
    else:
        return array([0.0, 0.0, 0.0])
