# Write a Hangman game in Python.
# Users should have a limited amount of attempts to guess a pre-defined word.
# Print feedback to the user when they made a guess,
# and keep track of and communicate their remaining attempts.

# Hard-code a word that needs to be guessed in the script
word = "Hazelnut"

# Print an explanation to the user
print("Welcome to this hangman game, where you have to guess the secret word. You'll guess one letter at a time with a total of 20 guesses. Lets begin!")

# Display the word as a sequence of blanks, e.g. "_ _ _ _ _" for "hello"
secret = ""
for i in range(len(word)):
    secret += "_ "
print(secret)

# Create a counter for how many tries a user has
counter = 21

# Keep asking them for their guess until they won or lost
while True:
    if secret.find("_")==-1:
        print("Congratulations!!\n you gueesed the word!")
        break
    counter -= 1
    if counter==0:
        print("Sorry you are all out of guesses. Try again some other time")
        break
    print("Guesses left:",counter,"\n")


# Ask for user input
    letter = input ("What letter do you chose?: ")

# Allow only single-character alphabetic input
    if len(letter)>1 or letter.isalpha()==False:
        print("Guesses may only contain single letters")
        continue

# When they find a correct character, display the blank with the word
#   filled in, e.g.: "_ e _ _ _" if they guessed "e" from "hello"
    elif word.find(letter)!=-1:
        for letter_s in range(len(word)):
            if word[letter_s] == letter:
                letter_index = -((len(word)-letter_s)*2-1)
                secret = secret[:letter_index-1]+letter.upper()+secret[letter_index:]
        print(secret)
        #print(secret)
    else:
        print(f"Sorry, {letter.upper()} is not contained in the word")



# Display a winning message and the full word if they win

# Display a losing message and quit the game if they don't make it
