# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.
x = int(input("Write a number: "))

if x%3==0:
    print(x/3)
else:
    print("not divisible")


