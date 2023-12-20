# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random
t=0

while True:
    y = int(input("Enter a number between 1 and 12: "))
    if y == random.randint(1, 12):
        print(f"congratz you guessed it, the number was: {y}")
        break
    elif t==10:
        print("No more attempts this time. Come back agian soon!")
        break
    else:
        t+=1
        print(f"So close, try again, you have {10-t} attempts left")
