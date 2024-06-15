# common_statistics.py
# functions for these already exist.. just practice
#mean median and mode

import collections

import numpy as np


#average
def mean(s):
    return np.sum(s) / len(s)

#middle of the sequence
def median(s):
    s.sort()
    i = len(s) // 2
    if len(s) % 2 == 1:
        return s[i]
    else:
        return (s[i - 1] + s[i]) / 2

#most appearances
def mode(s):
    c = collections.Counter(s)
    max_c = max(c.values())
    if max_c == 1:
        return None
    else:
        return [k for k, v in c.items() if v == max_c]


def main():
    # preferred way of creating random numbers in numpy
    rng = np.random.default_rng()
    a = rng.integers(low=1, high=100, size=30, endpoint=True)

    print(f"a = {a}")
    print(f"{mean(a) = }")
    print(f"{median(a) = }")
    print(f"{mode(a) = }")


main()
