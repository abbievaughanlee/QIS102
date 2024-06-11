# newton_sqrt.py

import numpy as np


def sqrt(x):
    # tuple
    low, high = 0, x
    est = (low + high) / 2
    # if estimate squared minus x is greater than the error, keep looping
    while np.abs(est**2 - x) > 1e-10:
        if est**2 < x:
            # if estimate squared is less than x, the low approximation becomes the estimate
            low = est
        else:
            # otherwise, the high approximation becomes the estimate
            high = est
        # finally, the estimate becomes the average between the low and the high
        est = (low + high) / 2
    # return the estimate
    return est


def main():
    x = 168923.74
    print(x)
    print(sqrt(x))


main()
