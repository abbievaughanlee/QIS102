# complex_factorization.py

import numpy as np
from sympy import prime

num_odd_primes = 25

# Use a list comprehension to generate the first 'n' odd primes
# Note: in sympy, prime(1) = 2, prime(2) = 3, etc.
primes = [int(prime(n)) for n in range(2, num_odd_primes + 2)]

# prints the "weak primes"
for p in primes:
    for a in range(1, int(np.sqrt(p))):
        b = np.sqrt(p - a**2)
        if b == np.floor(b):
            z1 = complex(a, b)
            z2 = complex(a, -b)
            print(f"{p:>3} = {z1}{z2}")
            break
# it turns out that all of the weak primes are of the form p = 8n - 3, n in Z+
