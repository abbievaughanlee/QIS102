# goldbach_conjecture.py

# every even integer > 4 can be written as the sum of two odd primes

from itertools import combinations_with_replacement

import numpy as np
from sympy import prime

test_limit = 100

print("Verifying Goldbach's conjecture for every EVEN ", end="")
print(f"integer from 6 to {test_limit} inclusive:")

# Use a list comprehension to create an array of the first 'n' primes
# creates a list and then converts it to a numpy array (working outside in)... ensures that 2 isn't included bc for goldbach we need odd primes

primes = np.array([prime(n) for n in range(2, test_limit)])

# Generate all pairs of primes (with repetition)
# generates every possible combination of pairs of the entries of the primes array
# asterisk exhaustively calls the function until there is no more remaining

prime_pairs = [*combinations_with_replacement(primes, 2)]

# Create sorted array containing the unique sums of each prime pairs
# for every pair in prime pairs, sum the pairs.
# create an array of these sums and ensure that each entry is unique
# sort this array

summed_pairs = np.sort(np.unique(np.array([sum(pair) for pair in prime_pairs])))

# Determine which EVEN integers from 6 to n (inclusive)
# are NOT in the list of summed prime pairs
# The numpy function setdiff1d() returns any elements in the first list
# that are not also in the second list

# check that each even number from 6 to the test limit is an element of the summed_pairs array

violations = np.setdiff1d(range(6, test_limit + 2, 2), summed_pairs)

# return whether or not violations were found

if len(violations) == 0:
    print("No Goldbach violations were found")
else:
    print(f"Found these violations: {violations}")
