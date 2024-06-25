# parallel_plates.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Rectangle
from scipy.ndimage import convolve, generate_binary_structure


# NEUMANN
def conductor_edges(a):
    # Carl Neumann (1832-1925)
    # A conductor forces the edges to
    # have zero potential (gradient=0)

    # ensure that along the outer edge of the walls, theres no change in voltage between adjacent cells
    # gradient is zero
    a[0, :] = a[1, :] # every cell against the wall and the cell to its immediate right have the same values
    a[-1, :] = a[-2, :]
    a[:, 0] = a[:, 1]
    a[:, -1] = a[:, -2]
    return a

#DIRICHLET
def insulator_edges(a):
    # Johann Dirichlet (1805-1859)
    # An insulator forces the edges to
    # have a fixed charge (voltage=0)
    # ensure that voltages are zero along the edges (gradient does not matter)
    a[0, :] = 0
    a[-1, :] = 0
    a[:, 0] = 0
    a[:, -1] = 0
    return a


def solve_laplace(ax, boundary_func): # boundary func either neumann or dirichlet
    # two parallel plates:
    left_volts = -1 
    right_volts = 1

    # world is a 100 by 100 discrete grid
    N = 100
    grid = np.zeros((N, N))
    # go from row 30 column 70 to row 29 column 30: vertical bar that is 40 units long and one unit wide
    grid[30:70, 29:30] = left_volts
    # 40 units down, 1 unit wide (parallel to left_volts)
    grid[30:70, 70:71] = right_volts

    # boolean indexing (all equal to either -1 or 1)
    mask_neg = grid == left_volts
    mask_pos = grid == right_volts

    kern = generate_binary_structure(2, 1).astype(float) / 4
    kern[1, 1] = 0

    # jacobi relaxation:
    # iterate 5000 times: keep pumping energy; walls will either let it pass or keep it in
    # keep doing this until system reaches steady state
        # zero-padding: the input grid is extended with zeros beyond its boundaries before the convolution operation
        # ensures that the kernel can overlap with all elements of the input grid including those near the edges
        # output size: the constant mode ensures the output grid is the same as the input grid
    iters = 5000
    for _ in range(iters):
        # Average every four neighbor cells in the grid
        grid_next = convolve(grid, kern, mode="constant")
        # Reapply the boundary conditions
        grid_next = boundary_func(grid_next)
        # Reapply the plate voltages
        grid_next[mask_neg] = left_volts
        grid_next[mask_pos] = right_volts
        # The next grid now becomes the new grid
        grid = grid_next

    # Render a colored contour plot of the electrostatic field potential
    surf = ax.contourf(range(N), range(N), grid, cmap="rainbow", levels=20)
    ax.get_figure().colorbar(surf, ax=ax, shrink=0.5) # see the colors as they relate to the voltage values

    # Blacken the two parallel plates
    ax.add_patch(Rectangle((29, 30), 1, 40, edgecolor="k", facecolor="k"))
    ax.add_patch(Rectangle((70, 30), 1, 40, edgecolor="k", facecolor="k"))

    # Title each graph
    if boundary_func == conductor_edges:
        ax.set_title("Conductor Edges")
    else:
        ax.set_title("Insulator Edges")

    ax.set_aspect("equal")


def main():
    plt.figure(Path(__file__).name, figsize=(10, 5.5))
    solve_laplace(plt.subplot(1, 2, 1), conductor_edges) # solve with the walls as conductors
    solve_laplace(plt.subplot(1, 2, 2), insulator_edges) # solve with the walls as insulators
    plt.tight_layout()
    plt.show()


main()
