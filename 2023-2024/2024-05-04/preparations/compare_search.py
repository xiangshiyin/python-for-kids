import random

def binary_search(arr, target):
    arr.sort()
    left = 0
    right = len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, steps
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, steps


def linear_search(arr, target):
    steps = 0
    for i in range(len(arr)):
        steps += 1
        if arr[i] == target:
            return i, steps
    return -1, steps

# Compare the number of steps to find the target number in 100 random sorted list of integers of increasing lengths using linear search and binary search

def compare_search():
    for i in range(10, 100000, 100):
        arr = [random.randint(0, i) for i in range(i)]
        target = random.randint(0, i)
        linear_search_steps = []
        binary_search_steps = []
        linear_search_steps.append(linear_search(arr, target)[1])
        binary_search_steps.append(binary_search(arr, target)[1])
    
        # print(f"Length: {i}, Linear Search: {sum(linear_search_steps)/len(linear_search_steps)}, Binary Search: {sum(binary_search_steps)/len(binary_search_steps)}")
    
    import matplotlib.pyplot as plt

    plt.plot(range(10, 100000, 100), linear_search_steps, label='Linear Search')    
    plt.plot(range(10, 100000, 100), binary_search_steps, label='Binary Search')
    plt.xlabel('Length of list')
    plt.ylabel('Number of steps')
    plt.title('Linear Search vs Binary Search')
    plt.legend()
    plt.show()


compare_search()
