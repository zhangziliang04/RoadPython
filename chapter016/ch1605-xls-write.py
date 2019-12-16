# -*- coding: utf-8 -*-

import xlwt
import sys

try:
    #01：创建工作薄
    f = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建工作簿
    #02：创建sheet
    sheet1 = f.add_sheet('sheet1', cell_overwrite_ok=True)  # 创建sheet
    row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计']
    #03：创建表头
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i])
    #04：创建第一列
    for i in range(1,100):
        sheet1.write(i,0,i)
    # xlsx格式不支持
    f.save('data\\ch1604-data-write.xls')  # 保存文件
    print("文件保存成功！")

except xlwt.ANTLRException as e:
    print("Error writing xls file : %s" % e)
    sys.exit(-1)