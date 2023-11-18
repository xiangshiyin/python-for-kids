students = {
    'Ryan': 10,
    'Jason':11,
    'Allen':12,
    'Philip':13
}

# name = 'Jason'
name = input("Enter a student name:\n")
# if name in students:
#     age = students[name]
#     print(f"{name} is {age} years old")
# else:
#     print(f"{name} is not in the class")

age = students.get(name, -1)
if age != -1:
    print(f"{name} is {age} years old")
else:
    print(f"{name} is not in the class")
