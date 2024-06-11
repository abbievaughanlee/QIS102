# big_sqrt.py

from mpmath import fabs, mp, mpf
#mpf- multi-precision floating point

def sqrt(x):
    #tuple of low and high: starts with 0.0 and x
    low, high = mpf("0.0"), x
    est = (high + low) / 2
    # epsilon is 100^(-100)
    epsilon = mpf(10 ** (-mp.dps / 2))
    #this is the same algorithm as newton_sqrt.py:
    while fabs(est**2 - x) > epsilon:
        if est**2 > x:
            high = est
        else:
            low = est
        est = (high + low) / 2
    return est


def main():
    #current precision
    mp.dps = 200  # dps = decimal places
    #declaration of a floating point integer (this is the number we are going to try and calculate the square root of)
    x = mpf(
        (
            "33590351381261822622218163873528556813698947665687"
            "61568876758902106044097938012929232223664368425159"
        )
    )
    print(x)
    print(sqrt(x))


main()
