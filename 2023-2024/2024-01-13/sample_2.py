def func(*args, **kwargs):
    print(f"args is of type: {type(args)}")
    print(f"args: {args}")
    print(f"kwargs is of type: {type(kwargs)}")
    print(f"kwargs: {kwargs}")

func(1,2,a=3,b=4)
