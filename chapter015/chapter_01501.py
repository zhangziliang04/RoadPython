# coding:utf-8
# ElementTree解析器：标签节点管理
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class ETreeHandler():
    def __init__(self):
        super().__init__()
        self.xml_path = None

    # 查找标签节点
    def select_node(self):
        """查询节点"""
        print("---------------select_node------------------")
        self.xml_path = "test.xml"
        # 通过获取tree对象
        tree = ET.parse(self.xml_path)
        # 获取根节点
        root = tree.getroot()
        # findall()：查找并迭代标签
        for data in root.findall('.//data'):  # xpath语法
            print(data)
        # find()： 查找满足条件的第一个标签
        data = root.find('.//data')
        print(data)

    # 删除标签节点
    def del_node(self):
        """添加节点"""
        print("---------------del_node------------------")
        self.xml_path = "test.xml"
        # 通过获取tree对象
        tree = ET.parse(self.xml_path)
        # 获取根节点
        root = tree.getroot()
        # 获取datas节点
        datas_node = root.find(".//datas")
        # 获取datas的第一个子节点
        data_node = root.find('.//datas/data')
        # 1.remove(节点对象)：删除指定的节点
        datas_node.remove(data_node)
        # 2.clear(): 清空datas下的所有子节点
        # datas_node.clear()
        # 回写xml数据
        tree.write("test3.xml", encoding='utf-8', xml_declaration=True)

    # 添加标签节点
    def add_node(self):
        print("---------------add_node------------------")
        self.xml_path = "test.xml"
        # 通过获取tree对象
        tree = ET.parse(self.xml_path)
        # 获取根节点
        root = tree.getroot()
        # Element(标签名):创建标签节点对象
        new_node = ET.Element("node")
        # 添加标签值
        new_node.text = "newNode"
        # 添加标签
        root.append(new_node)
        # 回写xml数据
        tree.write("test2.xml", encoding='utf-8', xml_declaration=True)


# 主函数
def main():
    etree = ETreeHandler()
    # 选择节点标签
    etree.select_node()
    # 添加节点标签
    etree.add_node()
    # 删除节点标签
    etree.del_node()


# 执行主函数
if __name__ == '__main__':
    main()