x = [9,8,7,6,5,4,3,2,1]
l = len(x)
threshold = (l - 1) // 2

for i in range(l):
    tmp = x[i]
    x[i] = x[l-1-i]
    x[l-1-i] = tmp
    print(f"i={i}, x={x}")
    if i == threshold:
        break
    # x[i], x[l-1-i] = x[l-1-i],x[i]

print(x)