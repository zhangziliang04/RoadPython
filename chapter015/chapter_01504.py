# -*- coding:utf-8 -*-
# XML DOM文件解析：实例程序
from xml.dom.minidom import parse
import xml.dom.minidom
import sys
file = "mysqlcon.xml"


# 先写一个判断节点是否包含element类型子节点的判断函数
def has_element_child(nodename):
    has_element_child = 0
    for child in nodename.childNodes:
        if child.nodeType == 1:
            has_element_child += 1
    return has_element_child


# 定义解析示例XML文件的方法
def parse_xml(filename):
    if not filename:
        sys.exit(0)
    tree = parse(filename)  # document类型的解析树
    root = tree.getElementsByTagName('proxool')[0]  # 将父节点定位到proxool element
    for child in root.childNodes:
        if child.nodeType == child.ELEMENT_NODE and has_element_child(child) == 0:  # 当node为element类型,且无element类型的子节点时
            print('配置项'+": %s" % child.tagName)
            print('配置值'+": %s" % child.firstChild.data.strip())
        elif child.nodeType == child.ELEMENT_NODE and has_element_child(child) > 0:     # 当节点包含element类型子节点时
            for child_child in child.childNodes:
                if child_child.nodeType == child.ELEMENT_NODE:
                    print('配置项'+": %s" % child_child.getAttribute('name'))
                    print('配置值'+": %s" % child_child.getAttribute('value'))
        elif child.nodeType == child.COMMENT_NODE:  # 当node为comment类型时
            print("--------------------------------------------------------")
            print('描述'+": %s" % child.data)
        else:
            pass


# 执行主函数
if __name__ == '__main__':
    parse_xml(file)

