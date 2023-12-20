# Use the built-in `sys` module to explicitly quit your script.
# Include this functionality into a loop where you're asking the user
# for input in an infinite `while` loop.
# If the user enters the word "quit", you can exit the program
# using a functionality provided by this module.

import sys
b=0

while True:
    if input("How many guesses do you need to write the password: ") == "quit":
        sys.exit("You got it! thumbs up!")
    b+=1
    print(b)