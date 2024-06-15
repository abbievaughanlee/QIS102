# uniform_variance.py

#Generate 15 sets of uniformly distributed random numbers where each set has a random size between 10_000 and 200_000 items
#calculate the "magic number" constant for each set: 
    #n = (upper_limit - lower_limit)^2 / variance

import numpy as np


def generate_set(set_num):
    #randoms set between 10_000 and 200_000 elements
    size = np.random.randint(10_000, 200_000)
    #set limits
    lower_limit = np.random.randint(10_000)
    upper_limit = lower_limit + np.random.randint(100_000)
    #create random set using limits and size specifications
    set = np.random.uniform(lower_limit, upper_limit, size)
    #set variables for the mean of the set and variance of the set
    m, v = np.mean(set), np.var(set)
    #calculate the magic number
    magic_number = (upper_limit - lower_limit) ** 2 / v
    #display information
    print(f"{set_num:>8}", end="")
    print(f"{size:>9,}", end="")
    print(f"{lower_limit:>9,}", end="")
    print(f"{upper_limit:>9,}", end="")
    print(f"{m:>12.3f}", end="")
    print(f"{v:>16.3f}", end="")
    print(f"{magic_number:>9.3f}")


def main():
    #headers
    print(f"{'Set #':>8}", end="")
    print(f"{'Size':>9}", end="")
    print(f"{'Lower':>9}", end="")
    print(f"{'Upper':>9}", end="")
    print(f"{'Mean':>12}", end="")
    print(f"{'Variance':>16}", end="")
    print(f"{'Magic':>9}")

    for set_num in range(1, 16):
        generate_set(set_num)


main()
