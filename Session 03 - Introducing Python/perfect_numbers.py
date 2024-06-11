# perfect_numbers.py
# write a program to calculate and display all the perfect numbers (elements of natural numbers) between 2 and 10,000
# an integer n is perfect when the sum of its proper divisors is equal to n
# 6 = 1 + 2 + 3


import numpy as np


def is_perfect(n):
    x = np.arange(1, n)
    # np.where returns the indexes where the expression is true
    factors = x[np.where(n % x == 0)]
    return np.sum(factors) == n


def main():
    for n in range(2, 10_000):
        if is_perfect(n):
            print(f"{n:,} is a perfect number")


main()

# given a perfect number n, what is the sum of the reciprocals of its divisors (including 1 and n)


def recip(n):
    # initialize variable sum, set it to zero
    sum = 0
    # ensure that the number passed is perfect
    if is_perfect(n):
        # iterate through the numbers 1 through n (inclusive)
        for i in range(1, n + 1):
            # check which numbers are divisors of n
            if n % i == 0:
                # add the reciprocal of any divisor to the sum
                sum += 1 / n
    # return the sum
    print(sum)


# call recip on some perfect number
recip(496)
