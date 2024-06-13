# random_walk.py
#display the 2D Cartesian plot of a meandering walker
#walker starts at the origin and takes one step at a time
#at each step, the walker picks a random angle and moves one unit of distance in that direction
#show the entire 10_000 random step journey
#on average, how far away from the start point will the walker stop

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

np.random.seed(2017)
#10_000 steps
n = 10_000
#create two arrays of 10_000 zeroes
x = np.zeros(n)
y = np.zeros(n)

#generates random angles for each step
for i in range(1, n):
    t = 2 * np.pi * np.random.rand()
    x[i] = x[i - 1] + np.cos(t)
    y[i] = y[i - 1] + np.sin(t)

#plots each step
plt.figure(Path(__file__).name)
#plots all of the points traveled
plt.plot(x, y)
plt.plot(x[0], y[0], color="green", marker="o")
#-1 -1 is the last value in the array (i.e the stop point)
plt.plot(x[-1], y[-1], color="red", marker="o")
# fmt: off
#plot an arrow from the start point to the last point
plt.arrow(x[0], y[0], x[-1] - x[0], y[-1] - y[0],
        color="black", linestyle="--",  width=0.3,
        head_width=1,  length_includes_head=True, zorder=3)
# fmt: on
plt.gca().set_aspect("equal")
plt.show()
