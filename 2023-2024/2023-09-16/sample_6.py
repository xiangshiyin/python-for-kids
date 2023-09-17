w1 = eval(input('The width of the 1st tier:\n'))
w2 = eval(input('The width of the 2nd tier:\n'))
w3 = eval(input('The width of the 3rd tier:\n'))

print('Here is the cake for you\n')
for i in range(9):
    if i // 3 == 0:
        print(('W'*w1).center(w3, ' '))
    if i // 3 == 1:
        print(('W'*w2).center(w3, ' '))
    if i//3 == 2:
        print(('W'*w3).center(w3, ' '))
