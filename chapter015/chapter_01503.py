# coding:utf-8
# ElementTree解析器：标签属性管理
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

    # 查询标签属性
    def select_attrib(self):
        """查询标签属性"""
        self.xml_path = "test.xml"
        # 通过获取tree对象
        tree = ET.parse(self.xml_path)
        # 获取根节点
        root = tree.getroot()
        # 获取标签属性
        attr_dict = root.attrib
        attr_key = root.keys()
        attr_item = root.items()
        attr_get = root.get('name')

        # 输出
        print(attr_dict)
        print(attr_key)
        print(attr_item)
        print(attr_get)

    # 添加/修改标签属性
    def update_attrib(self):
        """添加/修改标签属性"""
        self.xml_path = "test.xml"
        # 通过获取tree对象
        tree = ET.parse(self.xml_path)
        # 获取根节点
        root = tree.getroot()
        # 不存在则添加
        root.set("age", "30")
        # 存在则修改
        root.set("name", "mytest")
        # 回写xml数据
        tree.write("test4.xml", encoding='utf-8', xml_declaration=True)

    # 删除标签属性
    def del_attrib(self):
        """删除节点属性"""
        self.xml_path = "test.xml"
        # 通过获取tree对象
        tree = ET.parse(self.xml_path)
        # 获取根节点
        root = tree.getroot()
        # 删除名为name的属性
        del root.attrib["name"]
        # 回写xml数据
        tree.write("test5.xml", encoding='utf-8', xml_declaration=True)

    # 查询节点值
    def select_node_value(self):
        """查询节点值"""
        self.xml_path = "test.xml"
        # 通过获取tree对象
        tree = ET.parse(self.xml_path)
        # 获取根节点
        root = tree.getroot()
        # 获取第一个ip节点
        ip_node = root.find(".//ip")
        # 获取节点值
        node_value = ip_node.text
        print(node_value)

    def update_node_value(self):
        """添加/修改标签属性"""
        self.xml_path = "test.xml"
        # 通过获取tree对象
        tree = ET.parse(self.xml_path)
        # 获取根节点
        root = tree.getroot()
        # 获取第一个ip节点
        ip_node = root.find(".//ip")
        # 修改节点值
        ip_node.text = "10.1.1.1"
        # 回写xml数据
        tree.write("test6.xml", encoding='utf-8', xml_declaration=True)

# 主函数
def main():
    etree = ETreeHandler()
    '''
    # 选择节点标签
    etree.select_node()
    # 添加节点标签
    etree.add_node()
    # 删除节点标签
    etree.del_node()
    # 查询标签属性
    etree.select_attrib()
    '''
    # 查询标签值
    etree.select_node_value()


# 执行主函数
if __name__ == '__main__':
    main()
