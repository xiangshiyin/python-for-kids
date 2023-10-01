
import random

chances = 5
target = random.randint(1,100)
print(f"I'm think about a number between 1 and 100")
print(f"You have {chances} chances to guess the number in my mind!!")


previous_guess = 1e6
for i in range(chances):
    if i > 0:
        previous_guess = guess
    guess = eval(input('Guess the number in my mind:\n'))
    if guess == target:
        print('Bingo!')
        break
    else:
        # print('Keep trying')
        # if guess > target:
        #     print("Too big")
        # else:
        #     print("Too small")

        if abs(target - previous_guess) > abs(target - guess):
            print("Warmer")
        elif previous_guess == guess:
            print("Try a different number")
        else:
            print("Colder")
        if i == chances - 2:
            print("Only ONE CHANCE LEFT")
print(f'The answer is {target}')
