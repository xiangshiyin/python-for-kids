input_string = input("Type in a string:\n")

frequency = {}
for i in range(len(input_string)):
    character = input_string[i]
# for character in input_string:
    if character not in frequency:
        frequency[character] = 1
    else:
        frequency[character] += 1
print(f"The character frequencies is like this:\n{frequency}")

