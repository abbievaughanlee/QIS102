# leibniz_formula.py

#make sure that source code mimicks the mathematics as best as possible.

#QUESTION: what is 4* the leibniz sum????
import numpy as np

#creates an array
n = np.arange(1_000_000)

#vectorized operation
#creates a new array x: numerator of leibniz sum
x = (-1) ** n
#create a new array y: the denominator of the leibniz sum
y = 2 * n + 1

#now we can calculate the answer:
print(4 * np.sum(x / y))

#which, again, turns out to be pi!!
