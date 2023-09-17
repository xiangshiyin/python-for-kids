
first_string = input('Type in the 1st string:\n')
second_string = input('Type in the 2nd string:\n')
output = first_string in second_string
print(f"The evaluation result is: {output}")

if first_string in second_string:
    print(f"{first_string} is a part of {second_string}")
else:
    print(f"{first_string} is not a part of {second_string}")
