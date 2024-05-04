# use python to generate a list of random integers and implement linear search to find the given target number in the list
import random

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

arr = [random.randint(0, 100) for i in range(10)]
target = random.randint(0, 100)
print(arr)
print(target)
print(linear_search(arr, target))
