import random
words = [
    "sample",
    "python",
    "example",
    "programming",
    "coding",
    "science",
    "chinese"
]

word = random.choice(words)
chances = 5
guessed = []
print(f"##################GAME STARTED##################")
# we'll talk about function later
def display_current_word(word, guessed):
    current_word = ''
    # for i in range(len(word)):
    for char in word:
        # current_word += '_ '
        if char in guessed:
            current_word += char + ' '
        else:
            current_word += '_ '
    print(f"Current word to guess: {current_word}")
    return current_word

while chances > 0:
    # print the current word slots to guess
    current_word = display_current_word(word, guessed)

    if '_' not in current_word:
        print(f"Congratulations, you guessed the word CORRECT!!")
        break
    
    guess = input("Enter a letter:\n")
    if len(guess) > 1:
        print(f"Only one single letter allowed")
    guessed.append(guess)
    if guess not in word:
        chances -= 1
    print(f"Chances left: {chances}")

print(f"##################GAME OVER##################")
print(f"The word picked in this round is: {word}")