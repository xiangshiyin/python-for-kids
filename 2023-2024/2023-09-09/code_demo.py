# numbers and number operations
## 1. type() and sign flip
x = 123
type(x)

y = '123'
type(y)

x = -123
-x

## 2. pow() and ** operator to calculate exponent
pow(2,3)

2 ** 3

## 3. calculate the area of a circle
pi = 3.14
r = 100
area = pi * r * r
area

area = pi * pow(r, 2)
area

area = pi * (r ** 2)
area

## 3. who many numbers can a byte represent (1 byte = 8 bits, each bit could hold values of 0 or 1)
pow(2, 8)

2 ** 8


## 4. create string variables
x = 'my name is xxxx'
x


x = 'the weather is good'
x

y = "the weather is good"
y

type(x)
type(y)

## 5. triple-quotation marks
z = '''the weather is good'''
z

type(z)

x = '''this is the first line
this is the second line
this is the third line
this is the fourth line
'''
print(x)

## 6. can i create a multi-line string with single or double quotation marks??
y = 'this is the first line

## 7. special characters in string
x = "$"
y = "^"

x = '\n'
x = 'my name is apple\ni do not like banana'
print(x)


x = 'my name is apple\ti do not like banana'
print(x)


## 8. len() function to get the length of a string
x = 'hg;ahgpdhgohgohopghohwghopwhgp'
len(x)

## 9. single and double quotation marks are equivalent
x = 'abc'
y = "def"

## 10. combine 2 strings and create a longer string
x = 'apple'
y = 'banana'
z = x + y
print(z)

## 11. can i do x * y??
x * y

## 12. * opeartor could be used to repeat the same string pattern X times
x * 5

## 13. you can use lower() and upper() functions to transform the cases of string value
x = 'MY NAME IS APPLE'
x.lower()


y = 'my name is banana'
y.upper()

## 14. the in operator to check if a substring exists in a string
'c' in y

'name' in y

## 15. replace part of a string by something else
y.replace('banana', 'apple')

y.replace('banana', 'xxxx')

