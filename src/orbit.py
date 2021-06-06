"""
"""

# ---------- Imports ---------- #
from util import rotate_x, rotate_z
import numpy as np

# ---------- Constants ---------- #
R_E = 6371E3            # Radius of the Earth, [m]
MU = 3.986004418E14     # Standart gravitational parameter, [m^3/s^2]

# ---------- Classes ---------- #
class Orbit:
    """
    """

    def __init__(self, sma =R_E+400E3, ecc=0.0, inc=0.0, aop=0.0, lan=0.0, ta=0.0):
        self.sma = sma
        self.ecc = ecc
        self.inc = inc
        self.aop = aop
        self.lan = lan
        self.ta  = ta

    def radius(self):
        return self.sma*(1-self.ecc**2)/(1+self.ecc*np.cos(self.ta))

    def velocity(self):
        return np.sqrt(MU*((2/self.radius())-(1/self.sma)))

    def state_vec(self):

        # In-Plane state
        r = self.radius()
        v = self.velocity()

        # Rotation matrices
        rot_1 = rotate_z(self.lan)
        rot_2 = rotate_x(self.inc)
        rot_3 = rotate_z(self.aop)
        rotation = rot_1.dot(rot_2).dot(rot_3)

        # Position & Velocity
        p_vec = rotation.dot(np.array([[ r*np.cos(self.ta)], [r*np.sin(self.ta)], [0]]))

        # TODO: FIX THIS
        v_vec = rotation.dot(np.array([[-v*np.sin(self.ta)], [v*np.cos(self.ta)], [0]]))

        return np.vstack((p_vec, v_vec))
