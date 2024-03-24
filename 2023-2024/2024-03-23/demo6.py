import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("read_source.txt", "r") as file:
    lines = file.readlines()

# how many lines are there in the file
print(f"Number of lines: {len(lines)}")

# the last line
print(lines[-1])
