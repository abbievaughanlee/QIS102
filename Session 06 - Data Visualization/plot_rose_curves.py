# plot_rose_curves.py
#r = acosn0, r = asinn0, n even: 2n petals, n odd: n petals.. looks like a flower

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

#creates an array of 1000 numbers from 0 to 4pi
t = np.linspace(0, 4 * np.pi, 1000)
#three different rose curves
r1 = 4 + 4 * np.cos(4 * t)
r2 = 3 + 3 * np.cos(4 * t + np.pi)
#non-integer wave number
r3 = 5 + 5 * np.cos(3 / 2 * t)

plt.figure(Path(__file__).name)
#tell mathplotlib to switch its projection from cartesian to polar
plt.subplot(projection="polar")
plt.plot(t, r1)
plt.plot(t, r2)
plt.plot(t, r3)
plt.show()
