# print all non-negative even numbers that are less than 20

number = 0

while number < 20:
    if number % 2 == 0:
        print(f'The even number I found is {number}')
    number = number + 1
