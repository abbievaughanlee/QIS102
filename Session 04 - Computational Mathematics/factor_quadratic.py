# factor_quadratic.py

J = 115425
K = 3254121
L = 379020

print("Given the quadratic:")
print(f"{J}x^2 + {K}x + {L} = 0")
print("The factors are:")

found_factor = False

for a in range(1, J + 1):
    if J % a == 0:
        c = J // a
        for b in range(1, L + 1):
            if L % b == 0:
                d = L // b
                if a * d + b * c == K:
                    print(f"({a}x + {b})({c}x + {d})")
                    found_factor = True

if not found_factor:
    print("There are no factors.")
    print("The quadratic is prime.")
