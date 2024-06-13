# caesar_decrypt.py

from pathlib import Path

import numpy as np

file_name = "ciphertext2.txt"
#pick a shift
key_shift = -154

file_path = Path(__file__).parent / file_name
with open(file_path, "rb") as f_in:
    f_bytes = bytearray(f_in.read())

for i in np.arange(len(f_bytes)):
    #keeps within the bounds of the characters.. wraps around otherwise
    f_bytes[i] = (f_bytes[i] + key_shift) % 256

#decodes a byte array
print(f_bytes.decode("utf-8", "ignore"))
