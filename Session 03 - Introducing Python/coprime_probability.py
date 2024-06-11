# coprime_probability.py

#calculate the probability that two random natural numbers are coprime (their gcd ==1)

import numpy as np

#generate a million pairs of random integers
n = 1_000_000
#built into numpy: random.randint(Low, high, size, dtype)
#size is how many of the numbers you want (CREATES ARRAY)
#a and b are each arrays with 1,000,000 entries where each entry is a random integer between 1 and 1,000,000
a = np.random.randint(1, n, size=n)
b = np.random.randint(1, n, size=n)

#compares each element of a to each element of b and stores their gcd in a new array (still with 1,000,000 entries)
c = np.gcd(a, b)
#calculate the sum of all times that c is equal to 1 and divide it by the size of c
#this creates the probability that any two random integers are coprime
p = np.sum(c == 1) / c.size

#print the probability and format it as a percentage
print(f"Coprime Probability = {p:.2%}")
#display the "hidden constant" and format it with 4 spots to the right of the decimal
#hidden constant turns out to be pi again!!
print(f"Hidden constant     = {np.sqrt(6 / p):.4f}")
