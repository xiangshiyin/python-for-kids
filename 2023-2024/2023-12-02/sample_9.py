import math

def sumOfAList(numbers):
    # output = 0
    # for number in numbers:
    #     output += number # the summation
    output = sum(numbers)
    return output

result = sumOfAList([1,2,3,4,5,6,7,8,9,10])
print(f"The summation of all elements in the list is: {result}")
