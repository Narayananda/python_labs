# Decipher the message within the `secret` variable.
# Pick out only the alphabetic characters, not the numbers.

secret = "2349h30023388281e3299371l1l3094842o0333322883"
solution = ""

for i in range(len(secret)):
    if secret[i].isalpha():
        solution += secret[i]

print(solution)


