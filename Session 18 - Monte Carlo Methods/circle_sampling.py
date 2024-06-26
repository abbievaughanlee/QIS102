# circle_sampling.py
# suppose we want to generate random points known to be inside a unit circle centered at the origin
# instead of picking random cartesian coordinates for the sample points, we could use polar coordinates

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

n = 10_000
t = np.linspace(0, 2 * np.pi, n)
r = np.sqrt(np.random.rand(n))
x = r * np.cos(t)
y = r * np.sin(t)

plt.figure(Path(__file__).name)
plt.scatter(x, y, s=0.5)
plt.title("Uniform Circle Sampling")
plt.gca().set_aspect("equal")
plt.show()
