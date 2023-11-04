n = 10
prev = [1]

for i in range(n):
    print(str(prev).center(100))
    prev = [0] + prev + [0]
