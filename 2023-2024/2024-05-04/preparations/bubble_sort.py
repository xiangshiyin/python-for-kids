"""
Example

input: [5,4,3,2,1]
output: [1,2,3,4,5]
How do we do bubble sort?
Step 1: Find the smallest of all and put it to the beginning of the list
Step 2: Find the 2nd smallest of all and put it to the 2nd place of the list
...
Continue until all values are sorted
"""

import random

def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr

arr = [random.randint(1, 100) for _ in range(10)]
print(arr)
print(bubble_sort(arr))
