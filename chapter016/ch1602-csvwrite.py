#!/usr/bin/env python

import csv
import sys

filename = 'data//ch1602-data-write.csv'

# we open file with 'b' flag 
# for compatibility with non-linux users
try:
    with open(filename,'w',newline='') as f:
        writer = csv.writer(f)
        #写入表头
        header = ['id', 'date']
        writer.writerow(header)
        #写入文件内容
        for row in range(10):
            writer.writerow([row + 1, '2019-01-%s' % (19 + row)])
            print("写入行:%s" % row)
except csv.Error as e:
    print("Error writing CSV file at line %s: %s" % (row, e))
    sys.exit(-1)