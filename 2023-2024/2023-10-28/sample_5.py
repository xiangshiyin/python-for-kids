l1 = [0,1,2,1,0]
n1 = len(l1)
for i in range(n1):
    if i > 0:
        print(l1[i-1] + l1[i])