# std_cf.py
# standard continued fractions

import math

MAX_TERMS = 20


# normalizes the continued fraction
def normalize_cf(cf):
    while len(cf) > 2 and cf[-1] == 1 and cf[-2] != 1:
        cf[int(-2)] += 1
        cf.pop(-1)
    return cf


# encodes the continued fraction of a given number x
def encode_cf(x):
    # define cf as a list of integers
    cf: list[int] = []
    # continue with encoding until the length of the continued fraction is the desired number of max terms
    while len(cf) < MAX_TERMS:
        # put the floor of x into the cf list
        cf.append(int(x))
        # set x to x - floor(x)
        x = x - int(x)
        # if x == 0 end the encoding
        if x < 1e-11:
            break
        # set x to 1/x and continue looping
        x = 1 / x
    return normalize_cf(cf)


# decodes a continued fraction
def decode_cf(cf):
    # initialize variables
    h_n, k_n = 0, 0
    b_1, h_1, k_1 = 1, 1, 0
    h_2, k_2 = 0, 1
    # in a standard continued fraction, b_n is always 1
    # iterate through the terms of the continued fraction and adjust the variables accordingly
    for term in cf:
        a_n, b_n = term, 1
        h_n = a_n * h_1 + b_1 * h_2
        k_n = a_n * k_1 + b_1 * k_2
        b_1 = b_n
        h_1, h_2 = h_n, h_1
        k_1, k_2 = k_n, k_1
    # returns the continued fraction as a number
    return h_n / k_n


# evaluate the continued fraction of a given number x
def eval_cf(x):
    # call encode function on x
    cf = encode_cf(x)
    # after encoding x into a continued fraction, decode that continued fraction
    x2 = decode_cf(cf)
    # return x, its continued fraction, and the decoded x2 from that continued fraction
    print(f"{x} -> {cf} -> {x2}")


# test
def main():
    eval_cf(3.245)
    eval_cf(math.sqrt(2))
    eval_cf(math.sqrt(113))
    eval_cf(math.e)

    golden_ratio = (1 + math.sqrt(5)) / 2
    eval_cf(golden_ratio)


main()
