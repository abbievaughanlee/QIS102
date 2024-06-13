# board_encoding.py

# decodes a given integer representation of a specific configuration of a tic tac toe board
# 0 : square is open, 1 : X, 2 : O
# display the boards encoded as 2271, 1638, 12065

import numpy as np


# function to convert a given number to base 3
def base_three(n):
    # array to hold the digits
    to_return = np.zeros(9)
    # count to store digit place
    count = 8
    while n > 0:
        if count < 0:
            break
        if n % 3 != 0:
            to_return[count] = n % 3
            n = n / 3
            count -= 1
    return to_return
# use the base three number to create a board
print(base_three(3))