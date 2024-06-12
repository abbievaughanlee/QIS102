# plot_circle.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

#radius is 250
r = 250
#numpy array is created from 0 to 2pi with 1000 entries
t = np.linspace(0, 2 * np.pi, 1000)
#arrays of dependent variable values- the (x, y) Cartesian coordinates
#(note that these translate to the conversion between polar and cartesian coordinates of x and y)
x = r * np.cos(t)
y = r * np.sin(t)

#plot the circle
plt.figure(Path(__file__).name)
plt.plot(x, y)
plt.grid("on")
#by default, matplotlib does not respect the aspect ratio of your screen: this would cause the circle to look like an elipse
#gca means get current access
plt.gca().set_aspect("equal")
plt.show()
