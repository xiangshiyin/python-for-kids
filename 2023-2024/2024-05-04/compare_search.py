import random


def binary_search(alist, target):
    """
    alist: a list of integers
    target: the integer to search in the list

    output:
        return the position (index) of the number in the list

    Example:
        alist: [1,2,3,4,5]
        target: 4

        output: 3
    """
    l = 0
    r = len(alist) - 1
    steps = 0

    # sort the input list
    alist_copy = sorted(alist)

    while l <= r:
        steps += 1
        m = (l + r) // 2
        if alist_copy[m] == target:
            return m, steps
        elif alist_copy[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1, steps


def linear_search(alist, target):
    """
    alist: a list of integers
    target: the integer to search in the list

    output:
        return the position (index) of the number in the list

    Example:
        alist: [1,2,3,4,5]
        target: 4

        output: 3
    """
    l = len(alist)
    steps = 0
    for i in range(l):
        steps += 1
        if alist[i] == target:
            return i, steps
    return -1, steps


def experiment():
    steps_linear = []
    steps_binary = []
    # for length in range(100, 100000, 1000):
    for length in range(10, 100, 10):
        steps_linear_avg = 0
        steps_binary_avg = 0
        for trial in range(10):
            arr = [random.randint(0, length) for i in range(length)]
            target = random.randint(0, length)

            steps_linear_avg += linear_search(alist=arr, target=target)[1]
            steps_binary_avg += binary_search(alist=arr, target=target)[1]

        steps_linear.append(steps_linear_avg / 10)
        steps_binary.append(steps_binary_avg / 10)

    return steps_linear, steps_binary
    # print(f"linear: {steps_linear[1]}, binary: {steps_binary[1]}")


steps1, steps2 = experiment()
# print(steps1)
# print(steps2)

import matplotlib.pyplot as plt

# lengths = list(range(100, 100000, 1000))
lengths = list(range(10, 100, 10))
plt.plot(lengths, steps1, label="linear")
plt.plot(lengths, steps2, label="binary")
plt.xlabel("length")
plt.ylabel("steps")
plt.legend()
plt.show()
