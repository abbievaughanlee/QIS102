# plot_polynomial.py
#plots the same as plot_quintic.py but by using zeros and extrema points rather than equation

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import sympy

# Plot a polynomial with its zeros and extrema points
# Declare x to be a sympy symbol, not a python variable
x = sympy.symbols("x")

# Declare the polynomial "fn" by providing the coefficients
# of each term in in decreasing (exponent) order
fn_sym = sympy.Poly([1, -2, -120, 22, 2119, 1980], x)

# Find the real-only roots of the polynomial
# and store in a numpy array of floats
fn_zeros = np.array([float(r) for r in sympy.real_roots(fn_sym)])

# Find the symbolic first derivative of "fn" and locate the real-only
# zeros of this derivative to find the extrema (tangent) points
fn_d1 = sympy.Derivative(fn_sym, x, evaluate=True)
fn_d1_zeros = np.array([float(r) for r in sympy.real_roots(fn_d1)])

# Combine the zeros of "fn" and the zeros of the derivative of "fn" into a
# a single numpy array, then sort that array in increasing order. This array
# now contains the x-coordinate of interesting points in the "fn" polynomial
x_pts = np.sort(np.concatenate((fn_zeros, fn_d1_zeros)))

# Get the minimum and maximum of the interesting points array
x_min, x_max = x_pts[0] - 1, x_pts[-1] + 1
print(f"x_min = {x_min:.4f}, x_max = {x_max:.4f}")

x_vec = np.linspace(x_min, x_max, 1000)

# Create a numpy callable (numeric) function from the symbolic "fn" polynomial
fn_expr = fn_sym.as_expr()
fn_lambda = sympy.lambdify(x, fn_expr, modules="numpy")

# Plot the function
plt.figure(Path(__file__).name)
plt.plot(x_vec, fn_lambda(x_vec), linewidth=2)

# Plot the zeros and derivative roots
plt.scatter(fn_zeros, fn_lambda(fn_zeros), color="red")
plt.scatter(fn_d1_zeros, fn_lambda(fn_d1_zeros), color="green")

# Set the graph title to the polynomial expressed in LaTeX format
plt.title(f"$y = {sympy.latex(fn_expr)}$")

# Label the graph and draw (0,0) axis lines
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color="gray")
plt.axvline(0, color="gray")

plt.show()
