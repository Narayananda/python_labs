# Write a script that moves all files with the .png extension
# from one folder to another

# Import pathlib
import csv
from pathlib import Path

# Find the path to my Desktop
current_location = Path("C:\\users\\lucas\\Desktop")

# Create a new folder


dict_files = {}

# Filter for screenshots only
for file in current_location.iterdir():
    if file.suffix not in dict_files.keys():
        dict_files[file.suffix] = 1
    else:
         dict_files[file.suffix] += 1


with open("filecounts.csv", "a") as csvfile:
    countwriter = csv.writer(csvfile)
    data = []
    for file in dict_files:
        data.append(dict_files[file])
    countwriter.writerow(data)

with open("filecounts.csv","r") as csvfile:
    lines = csvfile.readline()
    # reader = csv.DictReader(csvfile, fieldnames=["Folder", "CSV", "MD","PNG"])
    # counts = list(reader)

print(lines)

# file_in = open("output.txt","r")
# content = file_in.read()
# content1=""
# for i in content:
#     if i == "{" or i=="'" or i == "\n":
#         continue
#     elif i == "}":
#         content1 += ","
#     else:
#         content1 += i

   
# content1 = content1.split(",")
# dict1 = {}

# for i in content1:
#     dict1[i[:i.index(":")]]=i[i.index(":"):]

# print(dict1)
# print(content)
# print(content1)

# file_in.close()








# for suffix in dict_files:
#     if dict_files[suffix] > 5:
#         valid_suffix = "".join(char for char in suffix if char.isalnum())
#         new_folder = Path(f"C:\\users\\lucas\\Desktop\\file_sort_script_{valid_suffix}")
#         new_folder.mkdir(exist_ok=True)
#         for file in current_location.iterdir():
#             if file.suffix == suffix:
#                 new_filepath = new_folder/file.name # Create a new path for each file
#                 file.replace(new_filepath) # Move the screenshot there
#                 print(file)


#--------------------------------------sencond iteration---------------------------------------
# To get that information, write a script that locates your Desktop, fetches all the files that are on there, 
# and counts how many files of each different file type are on your desktop. Use a dictionary to collect this data, 
# and print it to your console at the end in order to get an overview of what is there.

# You can now expand on your file mover script and add logic that moves all file types that have e.g. 
# more than five files on the desktop into their own separate folder. Will it help to keep your desktop cleaner?