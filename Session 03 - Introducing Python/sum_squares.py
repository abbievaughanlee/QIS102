# sum_squares.py
# sum the first 1000 natural numbers squared

import numpy as np

#initialize sum to 0

sum = 0
#iterate through the first 1000 natural numbers and add their squared value to the sum

for i in range(0, 1001):
    sum += i**2

# create the sum as determined by gauss' formula
n = 1000
gauss_sum = (2*(n**3) + 3*(n**2) + n)/6

# format the output of the two sums using a comma as the thousands separator

print(f"Loop: {sum:,}")
print(f"Gauss' formula: {gauss_sum:,}")

# check to ensure that the two calculations are equivalent
print(sum == gauss_sum)
