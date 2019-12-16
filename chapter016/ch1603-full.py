# -*- coding: UTF-8 -*-
import csv
import os
import sys
#读取CSV文件
def CsvReader():
    try:
        #csv_reader = csv.reader(open("ch1603-data.csv",'r', encoding='UTF-8'))
        with open("data\\ch1603-data.csv",'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                #01:读取整行
                print(row)
                #02:读取单列
                length = len(row)   #列数data//
                column = row[0]     #读取第1列
                print(length)       #打印列数
                print(column)       #打印第1列
    except csv.Error as e:
        print("Error reading CSV file at line %s: %s" % (reader.line_num, e))
        sys.exit(-1)

#写入CSV文件
def CsvWriteCSV():
    current_dir = os.path.abspath('.')
    #print(current_dir)
    file_name = os.path.join(current_dir, "data\\ch1603-data-write.csv")
    #print(file_name)
    #csvfile = open(file_name, 'wt',newline='' ,encoding="UTF8")  #
    try:
        with open(file_name, 'wt',newline='')  as csvfile1:
            header = ['股票代码', '干系人类型']
            writer = csv.writer(csvfile1)
            #writer.writerow(header)
            with open("data\\ch1603-data.csv",'r') as csvfile:
                reader = csv.reader(csvfile)
                for row in reader:
                    print(row)
                    csvrow1 = []
                    csvrow1.append(row[0])
                    csvrow1.append(row[1])
                    writer.writerow(csvrow1)
    except csv.Error as e:
        print("Error writing CSV file at line %s" % e)
        sys.exit(-1)


if __name__=="__main__":
    #读取方式1
    #CsvReader()
    #存储CSV
    CsvWriteCSV()


