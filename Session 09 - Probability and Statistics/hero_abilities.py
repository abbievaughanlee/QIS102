# hero_abilities.py
# str, dex, con, int, wis, cha
# roll a 20-sided die just once (for each attribute) but reroll if face value is 1, 2, 19, or 20
# OR: roll a six sided die three times per attribute and sum the value of each roll
# consider a program to generate a million hero ability score comparing the mean and standard deviation of each option


import numpy as np

#1 million trials
n = 1_000_000
#three random consecutive 6-sided dice rolls
a = np.random.randint(1, 7, n)
a = a + np.random.randint(1, 7, n)
a = a + np.random.randint(1, 7, n)

#1 random 20 sided dice roll
b = np.random.randint(3, 19, n)

print(f"six sided dice mean: {np.mean(a)} and standard deviation: {np.std(a)}")
print(f"twenty sided dice man: {np.mean(b)} and standard deviation: {np.std(b)}")
