# ========== Imports ========== #
from math import sqrt, sin, cos, acos
from numpy import array, cross, vstack, rad2deg
from util import rotate_x, rotate_z, norm


# ========== Constants ========== #
MU = 3.986004418E14     # Standart gravitational parameter, [m^3/s^2]
PI = 3.14159265359      # Pi, [-]

# ========== Classes ========== #
class Orbit:
    """
    """

    def __init__(self, sma=0.0, ecc=0.0, inc=0.0, lan=0.0, aop=0.0, ta=0.0):
        self.sma = sma
        self.ecc = ecc
        self.inc = inc
        self.lan = lan
        self.aop = aop
        self.ta  = ta

    def radius(self):
        return self.sma*(1-self.ecc**2)/(1+self.ecc*cos(self.ta))

    def velocity(self):
        return sqrt(MU*((2/self.radius())-(1/self.sma)))

    def to_state_vec(self):

        # In-Plane state
        r = self.radius()
        v = self.velocity()

        # Rotation matrices
        rot_1 = rotate_z(self.lan)
        rot_2 = rotate_x(self.inc)
        rot_3 = rotate_z(self.aop)
        rotation = rot_1.dot(rot_2).dot(rot_3)

        # Position & Velocity
        p_vec = rotation.dot(array([[ r*cos(self.ta)], [r*sin(self.ta)], [0]]))

        # TODO: FIX THIS
        v_vec = rotation.dot(array([[-v*sin(self.ta)], [v*cos(self.ta)], [0]]))

        return vstack((p_vec, v_vec))

    def from_state_vec(self, x):
        # Vectors
        r_vec = x[0:3]
        v_vec = x[3:6]
        h_vec = cross(r_vec, v_vec)

        # Scalars
        r = norm(r_vec)
        v = norm(v_vec)
        h = norm(h_vec)

        # Orbital parameters
        self.sma = (r*MU)/(2*MU-v**2*r)
        self.inc = acos(h_vec[2]/h)

        if h_vec[0] >= 0.0:
            self.lan = acos(-h_vec[1]/sqrt(h_vec[0]**2+h_vec[1]**2))
        else:
            self.lan = 2*PI - acos(-h_vec[1]/sqrt(h_vec[0]**2+h_vec[1]**2))

        return (self.sma, -1, rad2deg(self.inc), rad2deg(self.lan), -1, -1)
