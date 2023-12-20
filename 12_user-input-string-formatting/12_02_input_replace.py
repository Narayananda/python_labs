# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

the_string = input("Write somthing here: ")
the_symbol = input("and a symbol: ")

for i in range(len(the_string)):
    if the_string[0]==the_string[i]:
        print(the_symbol, end="")
        continue
    print(the_string[i], end="")