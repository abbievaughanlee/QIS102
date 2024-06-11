# basel_series.py

import numpy as np

# creates an array that goes from 1 to 49,999
n = np.arange(1, 50_000)

# now we want to look at the harmonic series
# looks at every term and adds it all
y1 = np.sum(1 / n)

# sum the basel series
y2 = np.sum(1 / n**2)

# when we use an = sign after the variable with spaces on either side, it displays the actual value.

print(f"{y1 = }")
print(f"{y2 = }")

# now we can successfully calculate the square root of 6y2 as n nears 50,000, as asked
# it returns pi... how??
print(f"{np.sqrt(6 * y2) = }")
