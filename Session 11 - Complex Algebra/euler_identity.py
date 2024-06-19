# euler_identity.py
# approximate e**pi

import numpy as np
import scipy

x = np.arange(20) # term number

n = np.power(complex(0, np.pi), x) # numerator
d = scipy.special.factorial(x) # denominator
ez = np.sum(n / d)

ez = np.round(ez, 8)
print(ez)
