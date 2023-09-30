import random

chances = 5
print(f"You have {chances} chances to guess the number!!")
target = random.randint(1, 67)

last_guess = None
for i in range(chances):
    if i > 0:
        last_guess = guess
    guess = eval(input("Guess the number in my mind:\n"))
    if guess == target:
        print("Bingo!")
        break
    else:
        if i > 0:
            if abs(target - guess) < abs(target - last_guess):
                print("Warmer")
            else:
                print("Colder")
        print("Keep trying")
print(f"The answer is {target}")
