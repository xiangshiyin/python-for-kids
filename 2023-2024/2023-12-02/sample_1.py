def testfunc():
    global x
    x = 123
    print(f"x inside the function equals to {x}")
    x = x + 1
    print(f"x inside the function after the increment equals to {x}")


testfunc()

x += 1


print(f"The value of x outside the function is {x}")
