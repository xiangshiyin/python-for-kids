number = 0

# print all non-negative integers that are less than 10
while True:
    if number < 10:
        print(f"number = {number}")
    else:
        break

    number += 1

print("Program Stopped")
print(f"After the program stopped, number={number}")
