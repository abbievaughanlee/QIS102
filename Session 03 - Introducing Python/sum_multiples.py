# sum_multiples.py

# display the sum of all natural numbers less that 1900 that are divisible by both 7 and 11


# create sum variable and initialize it to 0

sum = 0

# iterate through the natural numbers from 1 to 1900 and determine which are divisible by 7 and 11
#if a number is divisible by both 7 and 11, add it to the sum

for i in range(1, 1900):
    if i % 7 == 0 and i % 11 == 0:
        sum += i

# return the sum

print(sum)
