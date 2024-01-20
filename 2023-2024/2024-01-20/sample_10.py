x = 124
def func():
    global x
    x = 123
    print(f"Inside the function, x= {x}")

func()
print(f"Outside the function, x= {x}")
