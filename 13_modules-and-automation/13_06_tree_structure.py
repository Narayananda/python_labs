# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.

from pathlib import Path  # line 1

# my_desktop = Path("C:\\Users\\lucas\\Desktop")

# for filepath in my_desktop.iterdir():
#     if filepath.suffix == ".py":
#         print(filepath)  # Corrected the variable name from 'filpath' to 'filepath'
#         print(str(my_desktop))
#     elif filepath.is_dir():  # Use 'is_dir' to check if it's a directory
#         my_desktop = my_desktop / filepath  # Use '/' to append the directory to the path
#         print(str(my_desktop))
#     else:
#         print(f"This file is not a .py: {filepath.name}")  # Added an f-string for better formatting
#         print(str(my_desktop))


def recursive_search(folder):
    for filepath in folder.iterdir():
        if filepath.suffix==".py":
            print(filepath)
        elif filepath.is_dir():
            recursive_search(filepath)

current_location = Path("C:\\users\\lucas\\Desktop")
recursive_search(current_location)




