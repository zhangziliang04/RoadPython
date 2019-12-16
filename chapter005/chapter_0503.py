# 循环语句
#
# 01.for
print("---------for-----------")
# TypeError: 'int' object is not iterable
'''
count = 10
for i in count:
    print(i)
    i = i + 1


'''


index = 0
numbers = [1, 3, 5, 7, 9, 11, 13, 20, 29]
for index in range(len(numbers)):
    print(numbers[index])


# 02.while
print("---------while-----------")
j = 0
counts = 10
while j < counts:
    print(j)
    j = j + 1
else:
    print('Else语句被执行，j = ', j)
