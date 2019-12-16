# 文件打开
file = open("hello.txt", "r")
print("open")
file.close()

# 文件写入 write()
print("--------- write ------------")
file = open("hello.txt", "a+")
file.write(" Python\n")
file.close()

# 文件写入 writelines()
print("--------- writelines ------------")
data = ["string1", "string2"]
file = open("hello.txt", "a+")
file.writelines(data)
# file.writelines([line+'\n' for line in data])    # 换行处理
file.close()


# 文件读取：read
print("--------- read------------")
file = open("hello.txt", "r")
context = file.read()
print(context)
file.close()

# 文件读取：readline
print("--------- readline------------")
file = open("hello.txt", "r")
line = file.readline()
print(line)
file.close()

# 文件读取：readlines 所有行，直到文件结束
print("--------- readlines------------")
file = open("hello.txt", "r")
line = file.readlines()
print(line)
file.close()

