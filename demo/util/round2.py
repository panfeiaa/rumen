"""
统计各种字符数量
需求：读取一个文本文件，统计读取内容包含多少个大小写字母，多少个数字字符，多少个汉字，多少个特殊字符

本模块使用方法：提供一个文件路径，实例化一个对象出来
"""


class CharNumber:
    """构造函数"""
    def __init__(self, path: str):
        # 使用类中的属性存储路径的值
        self.path = path
        # 使用一个变量存储读取的字符
        self.file_str = ""
        # 定义一个集合（dict）来存储个类型字符和数量
        self.number_dict = {'upper': 0, 'lower': 0, 'number': 0, 'chinese': 0, 'other': 0}

        self.read_file()
        self.get_char_number()

    def read_file(self):
        """读取文本文件"""
        # 使用异常处理架构来读取文件！
        try:
            # 使用open函数实现文件的读取
            with open(self.path, mode='r', encoding='utf-8') as fd:
                self.file_str = fd.read()
        except Exception as e:
            raise e

    def get_char_number(self):
        """计算各种类型字符的数量"""
        # 使用循环来遍历每一个字符，然后统计
        for char in self.file_str:
            # 条件选择的框架
            if (char >= 'A') and (char <= 'Z'):              # 1、大写字母
                self.number_dict['upper'] += 1
            elif (ord(char) >= 97) and (ord(char) <= 122):    # 2、小写字母,使用asscii码
                self.number_dict['lower'] += 1
            elif (ord(char) >= 48) and (ord(char) <= 57):    # 3、数字,使用asscii码
                self.number_dict['number'] += 1
            elif (char >= '\u4e00') and (char <= '\u9fa5'):  # 4、汉字在unicode编码里是4e00-9fa5
                self.number_dict['chinese'] += 1
            else:                                            # 5、其他
                self.number_dict['other'] += 1
