# break
print("----------break--------------")
index = 0
numbers = [1, 3, 5, 7, 9, 11, 13, 20, 29]
for index in range(len(numbers)):
    if index == 3:
        break
    print(numbers[index])

# continue
print("----------continue--------------")
index = 0
numbers = [1, 3, 5, 7, 9, 11, 13, 20, 29]
for index in range(len(numbers)):
    if index == 3:
        continue
    print(numbers[index])

# pass
print("----------pass--------------")
index = 0
numbers = [1, 3, 5, 7, 9, 11, 13, 20, 29]

for index in range(len(numbers)):
    if index == 3:
        pass
    print(numbers[index])