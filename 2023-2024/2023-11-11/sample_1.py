import random

words = ["hello", "guess", "python", "hangman", "computer", "science"]
word = random.choice(words)
attempts = len(word)
guessed_letters = []

print(f"The selected word is {word}")

while attempts > 0:
    current_word_to_guess = ""
    for c in word:
        if c in guessed_letters:
            current_word_to_guess += c
        else:
            current_word_to_guess += "_"
    if "_" not in current_word_to_guess:
        print(f"Congratulations, you guessed the word: {word}")
        break
    print(
        f"""
        Current word to guess: {current_word_to_guess}
        Attempts left: {attempts}
    """
    )

    guess = input("Enter a letter:\n")
    if guess not in word:
        print("Wrong guess")
    guessed_letters.append(guess)
    attempts -= 1

if "_" not in current_word_to_guess:
    print(f"Congratulations, you guessed the word: {word}")
else:
    print(f"Sorry, you ran out of attempts. The correct answer is: {word}")
