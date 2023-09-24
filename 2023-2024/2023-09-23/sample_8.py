
import random

chances = 5
# target = 27
target = random.randint(1,67)

for i in range(chances):
    guess = eval(input('Guess the number in my mind:\n'))
    if guess == target:
        print('Bingo!')
        break
    else:
        print('Keep trying')
print(f'The answer is {target}')
