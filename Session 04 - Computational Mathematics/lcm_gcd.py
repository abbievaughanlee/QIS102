# lcm_gcd.py

import numpy as np

# calculate the lowest common multiple of two integers

# function that will calculate lcm given two integer inputs


def lcm(x, y):
    # store gcd of x and y
    greatest = np.gcd(x, y)
    # calculate lcm given gcd
    lowest = (np.abs(x * y)) / greatest
    print(lowest)


# test
lcm(447618, 2011835)
