"""
读取文件的工具类
"""


class ReadData:
    def __init__(self, path: str, infos: list):
        self.path = path
        self.infos = infos
        # 定义存储结果集合
        self.student_list = []
        self.student_dict = []

    def read_txt_file(self):
        """读取文本文件和csv文件"""
        # 异常处理结构
        try:
            with open(self.path, 'r', encoding= 'utf-8') as fd:
                # 读取第一行
                one_line = fd.readline()
                while one_line:  # 判断是否文件有数据
                    # 处理数据
                    one_line_list = one_line.strip().split("\t")
                    # 1、存储为list(list)
                    self.student_list.append(one_line_list)
                    # 2、存储为list(dict)
                    # 2.1 定义一个临时字典集合
                    temp_dict = {}
                    # 2.2 遍历,将key的list的索引和数据list的索引对应赋值
                    for index, value in enumerate(self.infos):
                        temp_dict[value] = one_line_list[index]   # 把value值作为key给了temp_dict字典，索引给他数据list去获取对应index的值。
                    # 2.3 附加到list
                    self.student_dict.append(temp_dict)
                    # 读取下一行
                    one_line = fd.readline()
        except Exception as e:
            raise e

