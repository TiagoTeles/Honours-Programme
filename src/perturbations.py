"""
"""

# ---------- Imports ---------- #
import numpy as np

# ---------- Constants ---------- #
R_E = 6371E3            # Radius of the Earth, [m]
MU = 3.986004418E14     # Standart gravitational parameter, [m^3/s^2]

# ---------- Function Definitions ---------- #

def radius(x):
    return np.sqrt(x[0]**2 + x[1]**2 + x[2]**2)

def velocity(x):
    return np.sqrt(x[3]**2 + x[4]**2 + x[5]**2)

def acc(x):
    return (-MU/radius(x)**3)*x[0:3]
