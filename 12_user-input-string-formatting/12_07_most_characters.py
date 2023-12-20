# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

one = input("write somthing: ")
two = input("do it again: ")
three = input("do it again: ")

if len(one)>len(two):
    if len(one)>len(three):
        print(len(one),one)
    else:
        print(len(three),three)
elif len(two)>len(three):
    print(len(two),two) 
else:
    print(len(three),three)