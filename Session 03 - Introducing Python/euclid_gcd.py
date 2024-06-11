# euclid_gcd.py

#euclid's algorithm for gcd: same as in discrete mathematics

def gcd(a, b):
    if a < b:
        #a convenient tuple to swap two values: Tuple packing/unpacking
        a, b = b, a
    c = a - b
    #we loop while c is greater than zero. Once c equals zero, we have found the gcd as the last remainder
    while c > 0:
        if c > b:
            a = c
        else:
            a = b
            b = c
        c = a - b
    #return the last b value (the remainder)
    return b

#faster way to determine gcd
def gcd_fast(a, b):
    while b > 0:
        #swap two values: a and the remainder of a divided by b
        a, b = b, a % b
    #returns the final remainder; i.e the gcd
    return a


def main():
    a, b = 182, 231
    print(f"The GCD of {a} and {b} = {gcd(a, b)}")
    print(f"The GCD of {a} and {b} = {gcd_fast(a, b)}")


main()
