
def calculator(num1, operator, num2):
    # recognize the operator
    if operator == '+':
        # do the calculation
        output = num1 + num2
    elif operator == '-':
        output = num1 - num2
    elif operator == '*':
        output = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print(f"Division by zero not allowed")
            return 1
        output = num1 / num2
    else:
        print(f"Invalid operator: {operator}")
        return 1

    # share the result (print or return)
    print(f"{num1} {operator} {num2} = {output}")

    return 0 # means success

status = calculator(num1=2, operator='/', num2=0)
print(f"Job status: {status}")
