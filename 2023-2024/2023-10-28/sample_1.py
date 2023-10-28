# Generate Fibonacci numbers

n = 1

counter = 1
f1 = 0
f2 = 1
while counter <= n:
    print(f1)
    tmp = f2
    f2 = f1 + f2
    f1 = tmp
    counter += 1
