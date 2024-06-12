# prime_racer3.py
# generate a list of 100_000 random integers in the range [1_000, 10_000]
# count # of prime numbers in that list
# measure total runtime in seconds

import math
import random
import time


#determines if a number is prime:
#testing if the number is even
#determines if an odd number has any divisors by iterating through all odd numbers less than the square root of n
def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        return all(n % factor != 0 for factor in range(3, int(math.sqrt(n)) + 1, 2))

# evaluates 100_000 random numbers in the given range and determines if they are prime
#runtime ~ 0.111
def main():
    random.seed(2016)
    num_primes = 0

    start_time = time.perf_counter()
    for _ in range(100_000):
        n = random.randint(1_000, 10_000)
        if is_prime(n):
            num_primes += 1
    elapsed_time = time.perf_counter() - start_time

    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}")


main()
