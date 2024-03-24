import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

file = open("read_source.txt", "r")

line = "_"

while line:
    line = file.readline()
    print(line)

file.close()
