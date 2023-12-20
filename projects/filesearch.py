# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.

from pathlib import Path

current_location = Path("C:\\users\\lucas\\Desktop")
py_files = "" # this string is going to act as a list that stores all the .py files we find.

for filepath in current_location.iterdir(): # first loop
    if filepath.suffix == ".py":
        py_files += f"{filepath.name}\n" # adds .py files to the empty sting that going to act like a list
    elif filepath.is_dir():
        current_location2 = current_location/filepath.name # since the file is a folder, we create a path to that folder so we can start a nested loop from that path.
        for filepath2 in current_location2.iterdir(): # first nested loop (means the we have entered the first folder)
            if filepath2.suffix == ".py":
                py_files += f"{filepath2.name}\n" # adds .py files to the empty sting that going to act like a list
            elif filepath2.is_dir():
                current_location3 = current_location2/filepath2.name
                for filepath3 in current_location3.iterdir(): # second nested loop (means the we have entered the second folder)
                    if filepath3.suffix == ".py":
                        py_files += f"{filepath3.name}\n" # adds .py files to the empty sting that going to act like a list
                    else:
                        break
            else:
                break

print(py_files)
    
    
