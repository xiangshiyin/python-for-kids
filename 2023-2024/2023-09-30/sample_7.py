
import random

chances = 5
target = random.randint(1,100)
print(f"I'm think about a number between 1 and 100")
print(f"You have {chances} chances to guess the number in my mind!!")



for i in range(chances):
    guess = eval(input('Guess the number in my mind:\n'))
    if guess == target:
        print('Bingo!')
        break
    else:
        # print('Keep trying')
        if guess > target:
            print("Too big")
        else:
            print("Too small")
        if i == chances - 2:
            print("Only ONE CHANCE LEFT")
print(f'The answer is {target}')
