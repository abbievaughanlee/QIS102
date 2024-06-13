# collatz_conjecture.py

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from numba import njit

#collatz conjecture: start with any integer greater than 1.
#if the number is even divide it by 2
#if the number is odd, multiply it by 3 and add 1
#the conjecture is that no matter what integer you start with, the process will always reach 1

#stopping time for an integer n: total  number of Collatz iterations before reaching 1
#stopping times exhibit a rough pattern but we have no formula to accurately predict it for any n
@njit
def stop_time(n):
    c = 0
    while n > 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        c = c + 1
    return c

#analyze the frequency of each stopping time for n < 1000000
#analyze the shape of the distribution of stopping times
def main():
    max_n = 1_000_000
    x = np.arange(max_n)
    # user functions are not inherently vector aware
    # np.vectorize allows user functions to be vector aware
    f = np.vectorize(stop_time)
    #f invokes stop time for all 1000000 numbers in x
    y = f(x)
    plt.figure(Path(__file__).name)
    #histogram: provides something that's countable
    #bins: takes all possible stop times and puts them into 500 bins (simplifies the graph)
    plt.hist(y, bins=500, color="blue")
    plt.title(f"Collatz Conjecture (n < {max_n:,})")
    plt.xlabel("Stopping Time")
    plt.ylabel("Count")
    plt.show()


main()
