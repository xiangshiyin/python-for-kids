import os
import string

os.chdir(os.path.dirname(os.path.abspath(__file__)))

translator = str.maketrans("", "", string.punctuation)
with open("hp_book1.txt", "r") as file:
    for line in file:
        x = line.translate(translator)
        print(x)
