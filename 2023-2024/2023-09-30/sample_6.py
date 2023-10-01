number = eval(input("Type in an integer:\n"))

if number % 2 == 0:
    print("divisible by 2")
elif number % 4 == 0:
    print("divisible by 4")
else:
    print("not divisible by 2 or 4")
