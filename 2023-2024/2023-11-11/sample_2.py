x = [1,2,3,4,5]
l = len(x)

# for i in range(l):
#     print(x[i])

# counter = 0
# while counter < l:
#     print(x[counter])
#     counter += 1

for idx, element in enumerate(x):
    print(f"idx={idx}, element={element}")
