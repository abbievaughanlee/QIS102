# euler_totient.py

import numpy as np

#totient of an integer is the number of positive integers less than the given integer that are relatively prime to that integer.
#task: calculate euler's totient for each integer between e and 100, inclusive
#the program should only display those integers whose value exceeds its own totient by exactly 1

def totient(n):
    s = 1
    # for loop introduces a scope with a colon :
    #never include n in a totient- works out because python is exclusive
    for i in range(2, n):
        #numpy gcd function.. numbers are coprime iff their gcd is equal to 1
        if np.gcd(i, n) == 1:
            s += 1
    return s


def main():
    print("Natural numbers between 2 and 100", end=" ")
    print("that exceed their totient by one:")

    for n in range(2, 101):
        #nested statements inside a scope are further indented
        if n == totient(n) + 1:
            print(n, end=" ")

#most important function: main

main()
