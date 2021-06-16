# ============================================================
# Name: Tiago Teles
# Email: T.MoreiraDaFonteFonsecaTeles@student.tudelft.nl
# Institution: Delft University of Technology
# License: GNU GPL 3.0
# ============================================================


# ========== Imports ========== #
import numpy as np
from orbit import Orbit
from simulation import Simulation


# ========== Main Program ========== #
if __name__ == "__main__":

    # Create a simulation
    simulation = Simulation(dt=1.0, t_final=24*3600)

    # Add an object to the simulation
    for i in range(1):
        simulation.add(Orbit(sma=6371E3+894E3, inc=11*np.pi/20))

    # Run simualtion
    result = simulation.run()

    # Plot orbits
    # simulation.animate_2d("XY")
    # simulation.animate_2d("YZ")
    # simulation.animate_2d("XZ")
    # simulation.animate_3d()
