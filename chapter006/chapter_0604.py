# 矩形输出
print("----------------------矩形输出---------------------------")
for i in range(1,10):
    for j in range(1,10):
        if i <= 9:
            print(f"{j}×{i} = {i * j}", end="\t")
    print("")
print("----------------------左下三角形---------------------------")
# 左下三角形式九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}×{i}={i*j}", end="\t")
    print(" ")

# 左上三角形式九九乘法表
print("----------------------左上三角形---------------------------")
for i in range(1,10):
    for j in range(i,10):
        print(f"{i}×{j}={i * j}", end="\t")
    print(" ")

# 右下三角形式九九乘法表
print("----------------------右下三角形---------------------------")
for i in range(1,10):
    for k in range(1,10-i):
        print(end="        ") #此处七个空格
    for j in range(1,i+1):
        print("%d×%d=%2d" % (i, j, i*j), end=" ")
        # 切记此处不能用格式化输出.format方式或者f"{}"， 要用格式化输出只能pycharm中才会显示下面的样式。
    print(" ")

# 右上三角形式九九乘法表
print("----------------------右上三角形---------------------------")
for i in range(1, 10):
    for k in range(1, i):
        print(end="        ")  #此处8个空格
    for j in range(i, 10):
        print("%d×%d=%2d" % (i, j, i * j), end=" ")  # 切记此处不能用格式化输出.format方式或者f"{}"， 要用格式化输出只能pycharm中才会显示下面的样式。
    print(" ")
