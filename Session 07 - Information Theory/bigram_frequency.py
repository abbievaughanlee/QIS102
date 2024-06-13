# bigram_frequency.py

from collections import Counter
from pathlib import Path

file_name = "bigram_ciphertext.txt"
print(f'Bigram analysis of file \n"{file_name}" :')

file_path = Path(__file__).parent / file_name
with open(file_path, "rb") as f_in:
    f_bytes = bytearray(f_in.read())

# Create Counter dictionary storing successive letter counts
bigrams = Counter()
for i in range(0, len(f_bytes) - 2):
    #less functionality- have to manage indices manually
    bigrams[(f_bytes[i], f_bytes[i + 1])] += 1

# Reverse sort bigrams tallied by Counter's dictionary item value,
# so the bigrams with the highest frequency appear first
# sort the bigrams so that the ones that appear most frequently are at the front
# sorted is built into python and enumerates through whatever sequence you give it
    #returns a tuple with inputs and how many times they ocurred
sorted_bigrams = sorted(bigrams.items(), key=lambda v: v[1], reverse=True)

# Print the top 10 most frequently occurring bigrams in text file
num_bigrams = sum(bigrams.values())
for k, v in sorted_bigrams[:10]:
    # Convert each key's value (a tuple of two ASCII values) to a string
    # NON-SHIFTED values!
    # Based on the frequencies, we can determine language.. from here we can completely decrypt
    s = "".join(map(chr, k))
    print(f'Bigram {k}, "{s}": freq = {v/num_bigrams:>5.2%}')
