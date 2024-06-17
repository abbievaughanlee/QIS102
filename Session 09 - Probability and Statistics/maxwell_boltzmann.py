# maxwell_boltzmann.py
# calculate and plot the probability density function of the Maxwell-Boltzmann distribution
# display three PDFs using parameters: a = 1, a = 2, a = 5\

import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


# PDF of maxwell boltzmann distribution
def pdf(x, a):
    #empty array to be later filled with y values
    to_return = []
    for i in x: #maxwell-boltzmann pdf formula
        to_return.append(
            math.sqrt(2 / math.pi)
            * ((i**2) / (a**3) * math.exp(-(i**2) / (2 * (a**2))))
        )
    return to_return

#create graphs
def main():
    # x values
    x = np.arange(0, 20, 0.1)

    # different parameters
    a1 = 1
    a2 = 2
    a3 = 5

    plt.figure(Path(__file__).name)
    #create three subplots for each of the parameters
    fig, (ax0, ax1, ax2) = plt.subplots(nrows=1, ncols=3, sharex=True, figsize=(14, 6))
    
    ax0.plot(x, pdf(x, a1))
    ax0.set_title("a = 1")
    ax0.set_xlabel("x")
    ax0.set_ylabel("PDF")
    ax0.set_xlim(0, 10) # ensure interval is set from 0 to 10 on the x-axis

   
    ax1.plot(x, pdf(x, a2))
    ax1.set_title("a = 2")
    ax1.set_xlabel("x")
    ax1.set_ylabel("PDF")
    ax1.set_xlim(0, 10)

    ax2.plot(x, pdf(x, a3))
    ax2.set_title("a = 5")
    ax2.set_xlabel("x")
    ax2.set_ylabel("PDF")
    ax2.set_xlim(0, 10)

    fig.suptitle("PDF of the Maxwell-Boltzmann Distribution")
    plt.show()


main()

