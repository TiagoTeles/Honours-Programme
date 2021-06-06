"""
"""

# Imports
import numpy as np

# Function definitionss
def rotate_x(a):
    return np.array([
        [1.0,       0.0,        0.0],
        [0.0, np.cos(a), -np.sin(a)],
        [0.0, np.sin(a),  np.cos(a)]])

def rotate_y(a):
    return np.array([
        [ np.cos(a), 0.0, np.sin(a)],
        [       0.0, 1.0,       0.0],
        [-np.sin(a), 0.0, np.cos(a)]])

def rotate_z(a):
    return np.array([
        [np.cos(a), -np.sin(a), 0.0],
        [np.sin(a),  np.cos(a), 0.0],
        [      0.0,        0.0, 1.0]])
