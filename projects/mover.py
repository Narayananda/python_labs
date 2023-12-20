# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
from pathlib import Path

# Find the path to my Desktop
current_location = Path("C:\\users\\lucas\\Desktop")

# Create a new folder
new_folder = Path("C:\\users\\lucas\\Desktop\\screenshot_python")
new_folder.mkdir(exist_ok=True)

# Filter for screenshots only
for screenshot in current_location.iterdir():
    if screenshot.suffix == ".png":
        new_filepath = new_folder/screenshot.name # Create a new path for each file
        screenshot.replace(new_filepath) # Move the screenshot there
        print(screenshot)