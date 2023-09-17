for i in range(10):
    if i < 5:
        print(('#' * (2* i + 1)).center(20, ' '))
    else:
        print(('#' * 5).center(20, ' '))