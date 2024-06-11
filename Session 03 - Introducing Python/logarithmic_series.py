# logarithmic_series.py
#What is the sum from k = 1 to 30 of 1 / ((2^k) * k) raised to the power s?

import numpy as np

#create  an array from 1 to 31, exclusive
#no step value written means that it will automatically be 1
k = np.arange(1, 31)
#sum the logarithmic series
s = np.sum(1 / (2**k * k))
#raise the series to the power s
print(np.exp(s))
