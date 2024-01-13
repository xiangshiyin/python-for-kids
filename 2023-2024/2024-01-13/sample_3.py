x = 123
y = 123.1
z = 'abc'
zz = "abc"
zzz = True
zzzz = False
# print(z == zz)

# print(type(zzz))

## a mutable data type (you can change it)
a = [1,2,3,4]
aa = ['a', 'b', 'c']
aaa = [1, 'a', 2, 'b']
aaaa = [[1,2], [3,4]]

## immutable data type
b = (1,2,3) # a tuple

## dictionary
c = {'a': 1, 'b': 2}

## condition
d = 4
if d % 2 == 0:
    print("It is an even number")
else:
    print("It is an odd number")

## loops - for/while
### for loop
for i in range(5):
    print("Hello")

counter = 0
while counter < 5:
    print('condition is met')
    counter += 1

# functions
def func(a, b):
    if a < b:
        print(f"{a} < {b}")
    else:
        print(f"{a} >= {b}")
    status = 0
    return status

return_value = func(a=3, b=2)
print(f"The status of the function run is {return_value}")
