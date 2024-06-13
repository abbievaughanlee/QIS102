# freq_histogram.py
# perform a histogram analysis: find out which letter occurs most frequently
# ignore ASCII value 32 (spaces)
# collections - can return a dictionary given an array with frequency of each element of the array
import collections
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

#text file
#file_name = "gettysburg.txt"
#analyze ciphertext1
file_name = "ciphertext2.txt"

# Read the data file into a buffer - construct a path to where the file is sitting
# pathlib division symbol (operator overloading) - almost like constructing a path on a terminal
# dunder file gives the whole path of the current script (freq_histogram.py).
# Then, go to the parent (QIS_labs)
# Then, append the file name (gettysburg.txt)

file_path = Path(__file__).parent / file_name
# Context manager- when you need to ask the system for a resource: ensures that even if it crashes, python cleans up
# r is read, b is binary: stored in the file f_in
with open(file_path, "rb") as f_in:
    #read the file that was just created - store it in a byte array (works for ASCII because every character is a byte)
    f_bytes = bytearray(f_in.read())
# Note - never closed  manually. The context manager does this explicitly


# Only set tick marks for characters that occur more than 6%
ticks = []
char_count = np.zeros(256)
for char, count in collections.Counter(f_bytes).items():
    char_count[char] = count
    if count / len(f_bytes) > 0.06:
        ticks.append(char)

# Create a histogram of each character's ASCII value
plt.figure(Path(__file__).name)
#bar chart made out of two arrays
plt.bar(np.arange(256), char_count)
#plot the ticks
plt.xticks(ticks)
plt.tick_params("x", rotation=90)
plt.title(f"Frequency Analysis ({file_name})")
plt.xlabel("ASCII Value")
plt.ylabel("Count")
plt.show()
