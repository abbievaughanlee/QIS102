# herons_formula.py
# use herons formula to calculate and display the lengths of every side and the area of 10 random triangles
# the length of each side of each triangle should be auniformly distributed random integer within 1 and 100 (inclusive)


from math import sqrt
from random import randint


# triangle is supposed to be a tuple of three integers
# -> specifies the return type
def is_triangle(triangle: tuple[int, int, int]) -> bool:
    # doc string: alternative to commenting- more helpful in some cases
    """Determine if a triangle is non-degenerate"""
    a, b, c = triangle
    return a + b > c and a + c > b and b + c > a


def area(triangle: tuple[int, int, int]) -> float:
    """Returns area of a triangle given a tuple of its three side lengths"""
    a, b, c = triangle
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))


def main() -> None:
    # underscore represents anonymous variable- if it were an i, it wouldn't matter
    # tells a reader that it will run 10 times, variable doesn't matter
    for _ in range(10):
        # walrus operator := allows you to define a variable inside the parameters of a function
        # can use in multiple places; anywhere where you have an assignment or creation of parameters or a conditional

        while not is_triangle(t := (randint(1, 100), randint(1, 100), randint(1, 100))):
            continue
        print(f"{t} {area(t):>9.4f}")


main()
