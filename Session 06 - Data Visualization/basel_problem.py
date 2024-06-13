# basel_problem.py
#sum of 1/n^2

import matplotlib.pyplot as plt
import numpy as np

#create 100000 instances
n = 100_000
#array of 10000 numbers from 1 to 100000
x = np.linspace(1, n, n)
y1 = np.cumsum(1 / x)
y2 = np.cumsum(1 / x**2)

#basel series converges to the value pi^2/6
print(np.sqrt(6 * y2[-1]))

plt.plot(x, y1, label="1/x")
plt.plot(x, y2, label="1/x**2")
plt.title("Infinite Series")
plt.xlabel("Number of Terms")
plt.ylabel("Cumulative Sum")
plt.legend(loc="center right")
plt.show()
