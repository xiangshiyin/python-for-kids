n = 10

f1 = 0
f2 = 1
for i in range(n):
    print(f1)
    tmp = f2
    f2 = f1 + f2
    f1 = tmp
