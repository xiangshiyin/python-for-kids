import matplotlib.pyplot as plt


def linear_search(alist, target):
    # assume it is a list of sorted integers
    steps = 0
    for number in alist:
        steps += 1
        if number == target:
            break
    return steps


# try different length values
lengths = list(range(1, 10000, 100))
steps = []
for length in lengths:
    step = linear_search(range(length), length)
    steps.append(step)

# print(steps)

plt.plot(lengths, steps)
plt.show()
