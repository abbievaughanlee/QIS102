# sum_squares.py
# sum the first 1000 natural numbers squared

import numpy as np

# create an array of the first 1000 natural numbers
numbers = np.arange(1, 1001, 1)

# create a sum of this array

sum = np.sum(numbers)

# create the sum as determined by gauss' formula

gauss_sum = 1000 * (1000 + 1) / 2

# format the output of the two sums using a comma as the thousands separator

print(f"Forced: {sum:,}")
print(f"Gauss' formula: {gauss_sum:,}")

# check to ensure that the two calculations are equivalent
print(sum == gauss_sum)
