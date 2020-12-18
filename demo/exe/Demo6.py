"""
dict字典集合使用
字典集合无序，key和value可以重复，若有相同的key，后输入的value值会覆盖老的value
"""

if __name__ == '__main__':
    dict01 = {'sno': 95001, 'name': 'Alice', 'birthday': '1992-9-30'}
    list01 = {95001, 'Alice', 'birthday', '1992-9-30'}

    print(dict01.keys())    # 获取所有keys
    print(dict01.values())  # 获取所有values
    print(dict01.items())   # 获取所有k-v

    print("=" * 20 + "第一种遍历的方法：")  # 打印中字符串后面跟数据会乘倍数
    for value in dict01.values():
        print("value的值", value)

    print("=" * 20 + "第二种遍历的方法：")
    for key in dict01.keys():
        print("key为", key, end="\t")  # 默認換行
        print("value的值", dict01[key])

    print("=" * 20 + "第三种遍历的方法：")
    for key, value in dict01.items():
        print("key为:", key, end="\t")
        print("value的值:", value)
