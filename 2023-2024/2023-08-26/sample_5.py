# collect input value from keyboard
input = eval(input("Type in a number:\n"))

# check if the input value is even or not
flag = input % 2

# if it is even, print the message "it is even"
# if it is odd, print the message "it is odd"
if flag == 0:
    print("it is even")
else:
    print("it is odd")
