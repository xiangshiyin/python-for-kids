sentence = input("Type in a sentence:\n")
words = sentence.split()
print(f"The sentence received is:\n{sentence}")
print(f"After tokenization, the list populated is:\n{words}")

frequency = {}
for word in words:
    if word not in frequency:
        frequency[word] = 1
    else:
        frequency[word] += 1
print(f"The word frequencies is like this:\n{frequency}")

