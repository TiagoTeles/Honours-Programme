"""
"""

# ---------- Imports ---------- #
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from perturbations import acc


# ---------- Constants ---------- #
LEO = 7371E3


# ---------- Function Definitions ----------- #
def update_2d(n, state, lines, step, x_index, y_index):
    """
    """
    start = time.time()
    for i, line in enumerate(lines):
        # Position vector
        p_vec = state[6*i:6*i+3, :]

        # Update lines
        x_data = p_vec[x_index, 0:n*step]
        y_data = p_vec[y_index, 0:n*step]

        line.set_data(np.array([x_data, y_data]))

    return lines


def update_3d(n, state, lines, step):
    """
    """

    for i, line in enumerate(lines):
        # Position vector
        p_vec = state[6*i:6*i+3, :]

        # Update lines
        line.set_data(p_vec[0:2, 0:n*step])
        line.set_3d_properties(p_vec[2, 0:n*step])

    return lines


# ---------- Classes ---------- #
class Simulation:
    """
    """

    orbits = []
    state = None
    n_obj = None


    def __init__(self, t_initial = 0.0, t_final = 3600.0, dt = 1.0):
        self.t_initial = t_initial
        self.t_final = t_final
        self.dt = dt
        self.n_iter = int((t_final-t_initial)/dt)


    def add(self, orbit):
        """
        """

        self.orbits.append(orbit)
        self.n_obj = len(self.orbits)


    def run(self):
        """
        """

        # Initialize
        start_time = time.time()
        self.state = np.zeros((6*self.n_obj, self.n_iter+1))

        # Setup initial conditions
        for i in range(self.n_obj):
            self.state[6*i:6*i+6] = self.orbits[i].state_vec()

        # Run simulation
        for i in range(self.n_iter):

            # Runge-Kutta coefficients
            k_1 = self.f(self.state[:, i])
            k_2 = self.f(self.state[:, i] + self.dt*k_1/2)
            k_3 = self.f(self.state[:, i] + self.dt*k_2/2)
            k_4 = self.f(self.state[:, i] + self.dt*k_3)

            # March in time
            self.state[:, i+1] = self.state[:, i] + (self.dt/6)*(k_1 + 2*k_2 + 2*k_3 + k_4)

        # Print execution time
        print("Execution time: " + str(time.time()-start_time) + " [s]")

        return self.state


    def f(self, x):
        """
        """

        f = np.zeros((6, self.n_obj))
        x = x.reshape((6, self.n_obj), order="F")

        for i in range(self.n_obj):
            f[0:3, i] = x[3:6, i]
            f[3:6, i] = acc(x[:, i])

        return f.flatten(order="F")


    def animate_2d(self, duration=10.0, fps=30.0, plane="XY"):
        """
        """

        # Determine correct plane
        index = {"X": 0, "Y": 1, "Z": 2}

        x_axis = plane[0]
        y_axis = plane[1]
        x_index = index[x_axis]
        y_index = index[y_axis]

        # Get axis
        axes = plt.gca()
        plt.tight_layout()

        # Setup plot
        axes.set_title("{}-{} Orbital Plane".format(x_axis, y_axis))
        axes.set_xlabel("{} Axis, [m]".format(x_axis))
        axes.set_ylabel("{} Axis, [m]".format(y_axis))
        axes.set_aspect("equal")

        # Axis limits
        axes.set_xlim(-2*LEO, 2*LEO)
        axes.set_ylim(-LEO, LEO)

        # Setup arguments
        n_obj = int(self.state.shape[0]/6)
        step = int(self.state.shape[1]/(fps*duration))

        lines = [axes.plot([], [])[0] for i in range(n_obj)]

        f_args = (self.state, lines, step, x_index, y_index)
        replay = animation.FuncAnimation(plt.gcf(), update_2d, fargs=f_args, interval=1000/fps)

        # Show animation
        plt.show()

        return replay

    def animate_3d(self, duration=10.0, fps=30.0):
        """
        """

        # Get axis
        axes = plt.gca(projection="3d")
        plt.tight_layout()

        # Title & Axis labels
        axes.set_title("3D Orbits")
        axes.set_xlabel("X Axis, [m]")
        axes.set_ylabel("Y Axis, [m]")
        axes.set_zlabel("Z Axis, [m]")

        # Axis limits
        axes.set_xlim(-LEO, LEO)
        axes.set_ylim(-LEO, LEO)
        axes.set_zlim(-LEO, LEO)

        # Setup arguments
        n_obj = int(self.state.shape[0]/6)
        step = int(self.state.shape[1]/(fps*duration))

        lines = [axes.plot([], [], [])[0] for i in range(n_obj)]

        f_args = (self.state, lines, step)
        replay = animation.FuncAnimation(plt.gcf(), update_3d, fargs=f_args, interval=1000/fps)

        # Show animation
        plt.show()

        return replay
