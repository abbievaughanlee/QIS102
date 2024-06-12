# celsius_to_farenheit.py

# convert a range of temperatures in the Celcius scale to the equivalent temperatures in the Farenheit scale.

import numpy as np

# create an array with temperatures between -44C and 104C, inclusive in steps of 4
c = np.arange(-44.00, 105.00, 4.00)

# create an array with the corresponding temperatures in farenheit
f = c * 1.80 + 32.0

# print each pair of values on its own line
for i in range(0, len(c)):
    print(f"Celcius: {c[i]}, Farenheit: {f[i]}")
