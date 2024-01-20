x = 122

print(f"x in outmost scope, begin: {x}")


def outer_func():
    x = 123
    print(f"x in outer_func(), begin: {x}")

    def inner_func():
        global x
        x += 2
        print(f"x in inner_func(): {x}")

    inner_func()

    print(f"x in outer_func(), end: {x}")


outer_func()
print(f"x in outmost scope, end: {x}")
