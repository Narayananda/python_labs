from pathlib import Path  # line 1

my_desktop = Path("C:\\Users\\lucas\\Desktop")

for filepath in my_desktop.iterdir():
    if filepath.suffix == ".pdf":
        print(filepath)  # Corrected the variable name from 'filpath' to 'filepath'

