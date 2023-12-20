# Ask the user to input their name. Then print a nice welcome message
# that welcomes them personally to your script.
# If a user enters more than one name, e.g. "firstname lastname",
# then use only their first name to overstep some personal boundaries
# in your welcome message.


#name = input("write your name: ")
#if name.find(" "):
 #   print(f"Silly {name[1:name.find(" ")]}, you should only print first name!")

#print(f"welcome {name} to this script")

name = input("Write your name: ")
if " " in name:
    print(f"Silly {name.split()[0]}, you should only print the first name!")  # line 3 <- error on this line, see below for error message
else:
    print(f"Welcome {name} to this script")

