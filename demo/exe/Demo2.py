"""
统计字符
"""

from util import round2
import os

if __name__ == '__main__':
    # 给一个文件路径
    basedir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    path = os.path.normpath("%s\/%s\/%s" % (basedir, '/file', "/file01.txt"))
    print(path)
    # 实例化一个对象
    obj = round2.CharNumber(path)
    # 读取文件
    try:
        # 读取
        obj.read_file()
        # 输出结果
        print("大写字母： %d\n小写字母: %d\n数字字符： %d\n汉字： %d\n其他字符：%d" %
              (obj.number_dict['upper'], obj.number_dict['lower'], obj.number_dict['number'],
               obj.number_dict['chinese'], obj.number_dict['other']))
    except Exception as e:
        print("读取文件出现异常，具体异常原因：" + str(e))
    # 输出内容
    print(obj.file_str)
