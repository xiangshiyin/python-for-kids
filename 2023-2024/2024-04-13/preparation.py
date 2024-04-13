import os
import string

os.chdir(os.path.dirname(os.path.abspath(__file__)))

words = []
with open("hp_book1.txt", "r") as file:
    for line in file:
        tokens = line.strip().split()
        for token in tokens:
            if token not in string.punctuation:
                words.append(token)

print(words[:10])
