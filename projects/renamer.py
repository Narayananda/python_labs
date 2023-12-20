# Move and rename all .png files on your Desktop
from pathlib import Path

current_location = Path("C:\\Users\\lucas\\Desktop")

# Create a new directory
new_folder = Path("C:\\Users\\lucas\\Desktop\\screenshots")
new_folder.mkdir(exist_ok=True)
i = 0

# Identify all screenshots on your Desktop and move and rename all screenshots

for screenshot in current_location.iterdir():
    if screenshot.suffix == ".png":
        i +=6
        new_name = screenshot.rename(f"{current_location}\\helloooo{i}.png")
        new_path = new_folder / new_name
        screenshot.replace(new_path)
        
