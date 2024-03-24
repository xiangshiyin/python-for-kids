import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

num_lines = 4
with open("read_source.txt", "r") as file:
    for i in range(num_lines):
        line = file.readline()
        if i == 3:
            print(line)
