# herons_method.py

#x = initial guess of root s = s/2
#s = (x + deltax)^2 = x^2 + 2x(delta x) + deltax^2
#deltax = (s - x^2)/(2x + deltax)
#assume deltax << x -> deltax is about (s - x^2)/(2x)
#much more efficient than newton's method

def sqrt(s):
    #set original estimate to be s / 2
    x = s / 2
    #epsilon is 1e-10
    while x**2 - s > 1e-10:
        #change x to the below formula while it is greater than epsilon
        x = (s / x + x) / 2
    return x


def main():
    x = 168923.74
    print(x)
    print(sqrt(x))


main()
