# -*- coding:utf-8 -*-
# XML DOM 文件编辑：实例程序
from xml.dom.minidom import parse
import xml.dom.minidom
import sys

old_file = "mysqlcon.xml"
new_file = "mysqlcon.new.xml"


# 先写一个判断节点是否包含element类型子节点的判断函数
def has_element_child(nodename):
    has_element_child = 0
    for child in nodename.childNodes:
        if child.nodeType == 1:
            has_element_child += 1
    return has_element_child


# 定义解析示例XML文件的方法
def match_xml(old_file, new_file):
    if not new_file:
        sys.exit(0)
    tree_old = parse(old_file)  # document类型的解析树
    tree_new = parse(new_file)
    root_old = tree_old.getElementsByTagName('proxool')[0]  # 将父节点定位到proxool
    root_new = tree_new.getElementsByTagName('proxool')[0]
    old_dict = {}   # 定义旧XML文件的tag和data的字典
    new_dict = {}
    for child in root_old.childNodes:   # 将tagName和data存入old_dict{}中
        if child.nodeType == child.ELEMENT_NODE and has_element_child(child) == 0:
            old_dict[child.tagName] = child.firstChild.data.replace("\n", "").replace("\t", "")
    for child in root_new.childNodes:
        if child.nodeType == child.ELEMENT_NODE and has_element_child(child) == 0:
            new_dict[child.tagName] = child.firstChild.data.replace("\n", "").replace("\t", "")
    for tag,data in new_dict.items():
        if not old_dict.get(tag):  # 当旧XML中找不到对应的tag时,进行tag新增操作
            new_element = tree_new.getElementsByTagName(tag)
            for child in new_element:
                root_old.appendChild(child)     # 新增element节点
    # 此处需要声明文件格式，否则乱码
    with open('mysqlcon_modified.xml', 'w', encoding='utf-8') as f:
        tree_old.writexml(f)


# 执行主函数
if __name__ == '__main__':
    match_xml(old_file,new_file)