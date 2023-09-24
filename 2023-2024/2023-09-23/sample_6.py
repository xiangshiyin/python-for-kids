str1 = input('Type in the first string:\n')
str2 = input('Type in the second string:\n')

l1 = len(str1)
l2 = len(str2)

for i in range(l2):
    # print(i)
    # print(str2[i])
    # print(str2[i:i+2])
    # print(str2[i:i+l1])
    segment = str2[i:i+l1]
    if segment == str1:
        print(f'I found str1 in str2 at position i={i}')
# if str1 is str1 of str2


# find out where str1 first appeared in str2
