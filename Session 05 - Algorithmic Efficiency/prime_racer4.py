# prime_racer4.py
# generate a list of 100_000 random integers in the range [1_000, 10_000]
# count # of prime numbers in that list
# measure total runtime in seconds

import math
import random
import time


#generates a list of prime numbers
def init_primes(max_n):
    known_primes = [2]
    for n in range(3, int(math.sqrt(max_n) + 1), 2):
        for factor in known_primes:
            if n % factor == 0:
                break
        else:
            known_primes.append(n)
    return known_primes

#determines if a number n is prime by iterating through the list of prime numbers
def is_prime(n, known_primes):
    if n % 2 == 0:
        return False
    else:
        return all(n % factor != 0 for factor in known_primes)

# evaluates 100_000 random numbers in the given range and determines if they are prime
# runtime ~ 0.093
def main():
    random.seed(2016)
    num_primes = 0
    #create a list of 10_0000 known primes
    known_primes = init_primes(10_000)

    start_time = time.perf_counter()
    for _ in range(100_000):
        n = random.randint(1_000, 10_000)
        if is_prime(n, known_primes):
            num_primes += 1
    elapsed_time = time.perf_counter() - start_time

    print(f"Number of primes found: {num_primes:,}")
    print(f"Total run time (sec): {elapsed_time:.3f}")


main()
