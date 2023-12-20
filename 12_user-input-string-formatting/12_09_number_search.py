# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

user_num = int(input("Enter a number: "))
iteration_num = 0

while iteration_num != user_num:
    iteration_num +=1
    print(iteration_num)
    

print(iteration_num)