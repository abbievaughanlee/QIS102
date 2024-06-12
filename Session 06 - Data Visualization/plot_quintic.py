# plot_quintic.py
#plots the same line as plot_polynomial.py 

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

#creates an array from -10 to 12
x = np.linspace(-10, 12)
# creates an array y of 50 values for each value of x
y = (x - 11) * (x - 5) * (x + 1) * (x + 4) * (x + 9)

#plots each x, y pair
plt.figure(Path(__file__).name)
plt.plot(x, y)
plt.grid("on")
plt.show()
