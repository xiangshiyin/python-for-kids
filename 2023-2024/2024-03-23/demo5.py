import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

line = "_"
with open("read_source.txt", "r") as file:
    while line:
        line = file.readline()
        print(line)
