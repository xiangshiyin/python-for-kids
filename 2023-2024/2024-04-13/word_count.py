import os
import string

os.chdir(os.path.dirname(os.path.abspath(__file__)))

filepath = "hp_book1.txt"
mode = "r"

words = {}  # the dictionary of word frequencies

with open(filepath, mode) as file:
    for line in file:
        # break the line into words
        for mark in string.punctuation:
            line = line.replace(mark, " ")
        tokens = line.lower().split()

        # update the dictionary with new words
        for token in tokens:
            # check if the token has been registered in the dictionary
            # if not, register it and assign frequency of 1
            # if yes, increment the frequency of this word by 1
            if token in words:
                words[token] += 1
            else:
                words[token] = 1

print(list(words.items())[0])

# words_sorted = {k: v for k, v in sorted(words.items(), key=lambda item: item[1], reverse=True)}
# print(words_sorted)

words2 = [(words[w], w) for w in words]
print(words2[:5])
words2.sort(reverse=True)
print(words2[:200])
