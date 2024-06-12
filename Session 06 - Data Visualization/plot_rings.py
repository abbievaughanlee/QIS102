# plot_rings.py
#plot the olympic rings


from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

# Draw the Olympic Rings
radius = 25.0
theta = np.linspace(0, 2 * np.pi, 1000)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

# offset between the centers
# top horizontal centers are offset by x, bottom horizontal centers are offset by x/2
# top and bottom centers are offset from each other by y
x_offset = 5 / 2 * radius
y_offset = radius

#plots the five circles based on the offsets
plt.figure(Path(__file__).name)
plt.plot(x, y, color="black", linewidth=12)
plt.plot(x - x_offset, y, color="blue", linewidth=12)
plt.plot(x + x_offset, y, color="red", linewidth=12)
plt.plot(x - x_offset / 2, y - y_offset, color="yellow", linewidth=12)
plt.plot(x + x_offset / 2, y - y_offset, color="green", linewidth=12)

plt.title("The Olympic Rings")
plt.gca().set_aspect("equal")
plt.axis(False)
plt.show()
