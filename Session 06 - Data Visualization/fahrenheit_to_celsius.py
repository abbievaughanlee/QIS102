# fahrenheit_to_celsius.py
#plot the Fahrenheit and Celsius temperature equivalents for temperatures in Kelvin from 0K to 400K
#plot labels the line graph of each temperature scale and shows a legend 

import matplotlib.pyplot as plt
import numpy as np

k = np.linspace(0, 400)
f = 9 / 5 * (k - 273.15) + 32
c = 5 / 9 * (f - 32)

plt.plot(k, f, label="Fahrenheit")
plt.plot(k, c, label="Celsius")

plt.title("Temperature Scale Comparison")
plt.xlabel("Kelvin")
plt.ylabel("Temperature")
plt.legend(loc="upper left")
plt.grid("on")
plt.show()
