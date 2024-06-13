# reverse_string.py

s1 = "Forever Young"
print(s1)

#iterate through the index backwards
s2 = ""
for i in range(len(s1) - 1, -1, -1):
    #add each last element of s1 to s2
    s2 = s2 + s1[i]
print(s2)

# iterates through s1 forwards, adds each character to the front of s3
s3 = ""
for c in s1:
    s3 = c + s3
print(s3)

#prints the characters of s1 in backwards order
print(s1[::-1])
