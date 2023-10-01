number = eval(input("Type in an integer here:\n"))

if number % 2 == 0:
    print("It is divisible by 2")
    if number % 4 == 0:
        print("It is divisible by 2 and 4")
    else:
        print("It is divisible by 2 but not 4")
else:
    if number % 4 == 0:
        print("It is divisible by 4")
    else:
        print("It is not divisble by 2 or 4")
