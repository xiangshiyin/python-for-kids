alist = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
found = 0  # not found

# go through the numbers in the list one by one
for number in alist:
    # check if the number matches the target
    if number == target:
        print("Found it")
        found = 1
        break

if found == 0:
    print("No match")
