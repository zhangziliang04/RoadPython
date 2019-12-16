# 嵌套循环

# for
print("----------for--------------")
for i in range(1, 10):
    for j in range(1, i+1):
        k = i*j
        print("%s*%s=%s" % (i, j, k), end=' ')
    print('i = %d' % i)

print("----------while--------------")
i = 1
j = 1
while i < 10:
    j = 1
    while j < i + 1:
        k = i * j
        print("%s*%s=%s" % (i, j, k), end=' ')
        j = j + 1
    i = i + 1
    print('i==%d' % i)



