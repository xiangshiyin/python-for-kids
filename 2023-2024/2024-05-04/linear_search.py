import random


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
    for i in range(l):
        if alist[i] == target:
            return i
    return -1


arr = [random.randint(0, 100) for i in range(10)]
target = random.randint(0, 100)

position = linear_search(alist=arr, target=target)
print(f"The list: {arr}")
print(f"The target: {target}")
print(f"Found target at position: {position}")
