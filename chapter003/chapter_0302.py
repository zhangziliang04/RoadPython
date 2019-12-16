# -*- coding: UTF-8 -*-
import keyword

#保留关键字
print(keyword.kwlist)


#行与缩进
if True:
    print("True")
else:
    print("False")

#缩进演示2
if True:
    print("Answer")
    print("True")
else:
    print("Answer")
    print("False")