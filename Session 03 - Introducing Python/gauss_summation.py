# gauss_summation.py
#calculate the "cumulative sum" series of the first 10 natural numbers
#show, term-by-term, the equivalence of these partial sums with their corresponding Gaussian summation values.


import numpy as np

n = 10
#create array from 1 to n, inclusive
x = np.arange(1, n + 1)
#print this array
print(x)

#create a cumulative sum of the array x
y1 = np.cumsum(x)
#print this array
print(y1)

#create a new array y2 which represents the cumulative sum as determined by gauss
y2 = x * (x + 1) / 2
print(y2)

#check if y1 and y2 match to determine if gauss is correct.
print(np.array_equal(y1, y2))
