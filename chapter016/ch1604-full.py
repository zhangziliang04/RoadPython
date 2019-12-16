# -*- coding: utf-8 -*-
import xlrd
import xlwt
import sys

from datetime import date, datetime
def read_excel():
    try:
        # 01-打开文件-1.工作薄.2.表sheet.3.行row列col.4.单元格cell
        workbook = xlrd.open_workbook("data\\ch1604-data.xlsx")
        # 02-获取所有sheet
        print(workbook.sheet_names())  # ['Sheet1', 'Sheet2', 'Sheet3']
        sheet_name = workbook.sheet_names()[0]
        # 根据sheet索引或者名称获取sheet内容
        sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
        sheet2 = workbook.sheet_by_name('Sheet1')

        # sheet的名称，行数，列数
        print(sheet2.name, sheet2.nrows, sheet2.ncols)
        #03-获取整行和整列的值（数组）
        rows = sheet2.row_values(3)  # 获取第四行内容
        cols = sheet2.col_values(0)  # 获取第1列内容
        print(rows)
        print(cols)
        #04-获取单元格内容
        print(sheet2.cell(1, 0).value)
        print(sheet2.cell_value(1, 0))
        print(sheet2.row(1)[0].value)
        # 获取单元格内容的数据类型
        print(sheet2.cell(1, 0).ctype)
    except xlrd.XLRDError as e:
        print("Error reading CSV file : %s" % e)
        sys.exit(-1)
'''
设置单元格样式
'''
def set_style(name, height, bold=False):
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = name  # 'Times New Roman'
    font.bold = bold
    font.color_index = 4
    font.height = height

    style.font = font
    # style.borders = borders
    return style
# 写excel
def write_excel():
    try:
        f = xlwt.Workbook(encoding='utf-8', style_compression=0)  # 创建工作簿
        #创建sheet
        sheet1 = f.add_sheet('sheet1', cell_overwrite_ok=True)  # 创建sheet
        row0 = [u'业务', u'状态', u'北京', u'上海', u'广州', u'深圳', u'状态小计', u'合计']
        column0 = [u'机票', u'船票', u'火车票', u'汽车票', u'其它']
        status = [u'预订', u'出票', u'退票', u'业务小计']
        # 生成第一行
        for i in range(0, len(row0)):
            sheet1.write(0, i, row0[i], set_style('Times New Roman', 220, True))
        # 生成第一列和最后一列(合并4行)
        i, j = 1, 0
        while i < 4 * len(column0) and j < len(column0):
            sheet1.write_merge(i, i + 3, 0, 0, column0[j], set_style('Arial', 220, True))  # 第一列
            sheet1.write_merge(i, i + 3, 7, 7)  # 最后一列"合计"
            i += 4
            j += 1
        sheet1.write_merge(21, 21, 0, 1, u'合计', set_style('Times New Roman', 220, True))
        # 生成第二列
        i = 0
        while i < 4 * len(column0):
            for j in range(0, len(status)):
                sheet1.write(j + i + 1, 1, status[j])
            i += 4
        #xlsx格式不支持
        f.save('data\\ch1604-data-write.xls')  # 保存文件

    except xlwt.ANTLRException as e:
        print("Error writing xls file : %s" % e)
        sys.exit(-1)
if __name__ == '__main__':
    #read_excel()
    write_excel()