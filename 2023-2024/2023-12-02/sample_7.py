
def calculator(num1, operator, num2):
    assert operator in ['+', '-', '*', '/'], f"Invalid operator: {operator}"
    assert operator != '/' or num2 != 0, f"Division by zero not allowed"

    # recognize the operator
    if operator == '+':
        # do the calculation
        output = num1 + num2
    elif operator == '-':
        output = num1 - num2
    elif operator == '*':
        output = num1 * num2
    elif operator == '/':
        output = num1 / num2

    # share the result (print or return)
    print(f"{num1} {operator} {num2} = {output}")

    return 0 # means success

status = calculator(num1=2, operator='/', num2=0)
print(f"Job status: {status}")
