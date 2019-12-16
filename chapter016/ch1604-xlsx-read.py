#!/usr/bin/env python
import xlrd
import sys
filename = 'data\\ch1604-data.xlsx'
try:
    # 01-打开文件-1.工作薄.2.表sheet.3.行row列col.4.单元格cell
    workbook = xlrd.open_workbook(filename)
    # 02-获取所有sheet
    print(workbook.sheet_names())  # ['Sheet1', 'Sheet2', 'Sheet3']
    sheet_name = workbook.sheet_names()[0]
    # 根据sheet索引或者名称获取sheet内容
    sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
    sheet2 = workbook.sheet_by_name('Sheet1')

    # sheet的名称，行数，列数
    print(sheet2.name, sheet2.nrows, sheet2.ncols)
    # 03-获取整行和整列的值（数组）
    rows = sheet2.row_values(3)  # 获取第四行内容
    cols = sheet2.col_values(0)  # 获取第1列内容
    print(rows)
    print(cols)
    # 04-获取单元格内容
    print(sheet2.cell(1, 0).value)
    print(sheet2.cell_value(1, 0))
    print(sheet2.row(1)[0].value)
    # 获取单元格内容的数据类型
    print(sheet2.cell(1, 0).ctype)
except xlrd.XLRDError as e:
    print("Error reading CSV file : %s" % e)
    sys.exit(-1)
