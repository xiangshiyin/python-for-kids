# Generate Fibonacci numbers

n = 10

if n == 0:
    print("")
elif n == 1:
    print(0)
else:
    counter = 0
    f1 = 0
    f2 = 1
    while counter < n:
        print(f1)
        tmp = f2
        f2 = f1 + f2
        f1 = tmp
        counter += 1
