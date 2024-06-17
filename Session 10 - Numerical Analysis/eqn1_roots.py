# eqn1_roots.py
# try to plot x**4 + x - 1
# in the real plane, we see only two zeros, so the other two roots must form a complex conjugate pair
    #solution: use both numpy and scipy

import numpy as np
from numpy.polynomial import Polynomial
from scipy.optimize import fsolve


def complex_formatter(x):
    if np.iscomplexobj(x) and np.imag(x) == 0: # we don't want 0.000j to be displayed for real numbers (stylistic choice)
        return f"{np.round(np.real(x), 4)}"
    else:
        return f"{np.round(x, 4)}"


np.set_printoptions(formatter={"complex_kind": complex_formatter}) #call complex formatter


def f(x):
    return x**4 + x - 1


print("Roots of f(x)")
print("Via scipy")
# SciPy fsolve() only shows two real roots
#fsolve requires a hint and can only find one real root at a time
print(fsolve(f, -1.5))
print(fsolve(f, 0.5))
print("Via numpy")
# It turns out f(x) truly has FOUR roots:
#  - Two distinct real roots
#  - Two complex roots (a conjugate pair)
p = Polynomial([-1, 1, 0, 0, 1])
roots = p.roots()
print(roots)
print("Valid roots")
print(roots[np.isclose(f(roots), 0)])
