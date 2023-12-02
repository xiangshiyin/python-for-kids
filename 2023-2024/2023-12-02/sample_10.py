def flipAList(numbers):
    length = len(numbers)
    l = 0
    r = length - 1
    while l < r:
        numbers[l], numbers[r] = numbers[r], numbers[l]
        l += 1
        r -= 1
    print(f"After the flip, the list becomes {numbers}")


flipAList(numbers = [1,2,3,4,5])
flipAList(numbers = [1,2,3,4,5,6,7,8,9,10])