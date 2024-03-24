import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with open("read_source.txt", "r") as file:
    content = file.read()

# the whole content
print(content)

# how many characters are there in the file
print(f"Number of characters: {len(content)}")

# the last character
print(content[-1])
