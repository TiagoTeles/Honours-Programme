# ============================================================
# Name: Tiago Teles
# Email: T.MoreiraDaFonteFonsecaTeles@student.tudelft.nl
# Institution: Delft University of Technology
# License: GNU GPL 3.0
# ============================================================

# ---------- Imports ---------- #
import time
import numpy as np

from simulation import Simulation
from orbit import Orbit

# ---------- Main Program ---------- #
if __name__ == "__main__":

    # Register start time
    start = time.time()

    # Create a simulation
    simulation = Simulation(dt = 1.0, t_final = 24*3600)

    # Add an object to the simulation
    simulation.add(Orbit(sma = 6371E3 + 400E3))

    # Run simualtion
    simulation.run()

    # Plot orbits
    simulation.animate_2d()
    simulation.animate_3d()
