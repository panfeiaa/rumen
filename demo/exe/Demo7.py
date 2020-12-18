"""
综合案例：系统需要使用学生信息，先要通过各种数据源获取学生数据，存储在list集合和dict集合中
1、从txt或者csv格式读取
2、从json文件读取
3、从excel文件读取
4、从mysql数据库读取
读取文本数据到list和dict
"""

import os
from util import ReadData

if __name__ == '__main__':
    path = "C:\\Users\\30524\\Desktop\\python\\student.txt"
    infos = ['sno', 'name', 'birthday', 'phone', 'mail', 'address']
    obj_student = ReadData.ReadData(path, infos)
    try:
        obj_student.read_txt_file()
        # 输出list
        print(obj_student.student_list)
        # 输出dict
        print("=" * 150)
        print(obj_student.student_dict)
    except Exception as e:
        print("读取文件出现异常，具体原因：", str(e))

