#rlc_circuit.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator
from scipy.integrate import solve_ivp


def model(t, y, R, L, C):
    # let i2 represent the derivative of i
    i = y[0] # = i(t)
    i2 = y[1] # = d(i)/dt

    return[(-i/(L*C)) - (R/L)*i2]


def main():
    # Set simulation constants
    R = 0.1
    L = 0.01
    C = 0.01

    # Set Initial Conditions
    i_0 = 1.0
    time_initial = 0
    time_final = 1

    # Solve eqn for I(t)
    sol = solve_ivp(
        model,
        (time_initial, time_final),
        [i_0, 0],
        max_step=0.01,
        args=(R, L, C),
    )
    
    
    # plot
    plt.figure(Path(__file__).name)
    plt.plot(sol.t, sol.y[0], color="blue", lw=2)
    plt.xlabel("time")
    plt.ylabel("current")
    plt.title("LCR Circuit")
    
    plt.show()


main()
