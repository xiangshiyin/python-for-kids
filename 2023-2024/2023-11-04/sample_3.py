x = [8,7,6,5,4,3,2,1]
l = len(x)
i = 0
j = l - 1

while i < j:
    tmp = x[i]
    x[i] = x[j]
    x[j] = tmp
    i = i + 1
    j = j - 1
    print(f"x={x}")
print(x)