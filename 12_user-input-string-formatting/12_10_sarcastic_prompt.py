# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.
opinion = input("Write your honest opinion: ")
for i in range(len(opinion)):
    if i%2==0:
        print(opinion[i], end="")
    else:
        print(opinion[i].upper(), end="")
