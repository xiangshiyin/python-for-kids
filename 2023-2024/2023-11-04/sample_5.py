pt = [[1]]
n = 10

for i in range(n):
    new_layer = []
    old_layer = [0] + pt[i] + [0]
    len_old_layer = len(old_layer)
    for j in range(len_old_layer):
        if j < len_old_layer - 1:
            new_layer.append(old_layer[j] + old_layer[j+1])
    pt.append(new_layer)

for k in range(len(pt)):
    print(str(pt[k]).center(100))