n = 0
f_0 = 0
f_1 = 1

while n < 10:
    if n == 0:
        print(f_0)
    elif n == 1:
        print(f_1)
    else:
        f_2 = f_1 + f_0
        print(f_2)
    n += 1
