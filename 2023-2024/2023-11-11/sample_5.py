word = 'sample'

current_word = ''
for i in range(len(word)):
    # current_word += word[i] + ' '
    # current_word += '_ '
    if word[i] in ['a', 'e']:
        current_word += word[i] + ' '
    else:
        current_word += '_ '
print(current_word)
