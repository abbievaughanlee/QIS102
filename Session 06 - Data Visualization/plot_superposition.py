# plot_superposition.py
#two sinusoids (waves) are placed in superposition (added together) 
#there is a trig identity called the angle product formula that allows us to represent the
#superposition of two sinusoids as the product of their respective wave functions
#study the behavior of the superposition r = 7 + 7sin(110)cos(50)
    #with the angle product identity this is equivalent to: 7 + (7/2)[sin(16t) + sin(6t)]

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

#generate an array from 0 to 4pi with 1000 entries
t = np.linspace(0, 4 * np.pi, 1000)
#store the superposition function as an array r
r = 7 + 7 * np.sin(11 * t) * np.cos(5 * t)

#plot r
plt.figure(Path(__file__).name)
plt.subplot(projection="polar")
plt.plot(t, r, color="black")
plt.show()
