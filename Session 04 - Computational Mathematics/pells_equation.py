# pells_equation.py
# find the minimum x & y for any given n such that x^2 - ny^2 = 1

from math import floor, sqrt

from numba import njit


# decorator allows for additional information about a function
# c-code
@njit
def pell_solution(n):
    x = 1
    while x < 70_000:
        x2 = x * x
        y = 1
        y_max = floor(sqrt((x2 - 1) / n))
        while y <= y_max:
            y2 = y * y
            if x2 - n * y2 == 1:
                # exit loop, set x and y as solutions
                return True, x, y
            y += 1
        x += 1
    # if no solution has been found for x < 70000 return false and no solution
    return False, 0, 0


def main():
    # print table headers
    print(f"{'n':>4}{'x':>8}{'y':>8}")
    print(f"{'='*3:>4}{'='*6:>8}{'='*6:>8}")
    # arrange n from 2 to 70
    for i in range(2, 71):
        solution_exists, xs, ys = pell_solution(i)
        if solution_exists:
            print(f"{i:>4}{xs:>8}{ys:>8}")
        else:
            print(f"{i:>4}{'-':>8}{'-':>8}")


main()
