# random_walk_lattice.py
#suppose the walker is constrained to taking unit steps in the four cardinal directions
#imagine each walk starts at the origin and that the total steps for each walk can vary from 1 to 200
#as a function of the number of steps taken, how far away from the origin will the average walk end
#we will take 50000 walks of each length and compute the average final Euclidian distance from the origin

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numba import njit


@njit
def get_avg_dist(dims, max_steps, num_walks):
    # Returns the mean final distance (normalized)
    # of (num_walks) uniform random walks having length (num_steps)
    # on a unit lattice having (dim) dimensions
    avg_dist = np.zeros(max_steps)
    for step in range(max_steps):
        total_dist = 0.0
        for _ in range(num_walks):
            steps = np.zeros(dims)
            for _ in range(step):
                # Take one step in some random dimension
                h = np.random.randint(0, dims)
                steps[h] += -1 if np.random.rand() < 0.5 else 1
            # Calculate straight-line distance traveled
            total_dist += np.sqrt(np.sum(np.power(steps, 2)))
        # Calculate average final distance for this number of steps
        avg_dist[step] = total_dist / num_walks
    return avg_dist


def fit_linear(x, y):
    n = len(x)
    m = float(n * np.sum(x * y) - np.sum(x) * np.sum(y))
    m /= float(n * np.sum(x**2) - np.sum(x) ** 2)
    b = float(np.sum(y) - m * np.sum(x))
    b /= n
    return m, b


def main():
    # Number of dimensions
    dims = 2

    # Walks increase in length from 1 to max_steps
    max_steps = 200

    # Number of times a walk of each length is repeated to find its average
    num_walks = 50_000

    print("This may take up to 30 seconds . . .")
    steps = np.arange(max_steps)
    distances = get_avg_dist(dims, max_steps, num_walks)
    distances_squared = distances**2

    m, b = fit_linear(steps, distances_squared)
    print(f"Slope of line = {m:.4f}")

    plt.figure(Path(__file__).name, figsize=(12, 5))

    # first number = number of rows of plots
    # second number = number of columns
    # third number
    ax = plt.subplot(1, 2, 1)
    ax.plot(steps, distances)
    ax.set_title(f"Uniform Random Walk on {dims}-D Unit Lattice")
    ax.set_xlabel("Number of Steps")
    ax.set_ylabel("Mean Final Distance")

    ax = plt.subplot(1, 2, 2)
    # y axis = distances squared
    ax.plot(steps, distances_squared, color="green")
    # y = mx + b
    ax.plot(steps, m * steps + b, color="red", linewidth=2)
    ax.set_title(rf"$Slope\;of\;Line\times{{4}}={4*m:.4f}$")
    ax.set_xlabel("Number of Steps")
    ax.set_ylabel(r"$(Mean\;Final\;Distance)^2$")

    plt.show()


main()
# Note: d_avg = sqrt(pi*n) / 2