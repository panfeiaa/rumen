"""
遍历list，对元素逐一访问
三种方式：
1、for in
2、for in range
3、for in enumerate
"""


if __name__ == '__main__':
    list01 = [11, 22, 33, 44, 55, 66, 77, 88, 99]
    # 遍历方式1：for in
    '''
        优点：最简单的   缺点：只能取值不能修改    
    '''
    for item in list01:
        print(item)

    # 遍历方式2：for in range
    '''
        优点：既可以渠道元素也可以通过索引修改。  缺点：要取索引比较麻烦
    '''
    for index in range(0, len(list01)):
        print("索引号：", index, "值：", list01[index])

    # 遍历方式2：for in enumerate
    '''
        最常用,直接取出索引和值，不需要用索引去取值，也好操作
    '''
    for index, item in enumerate(list01):
        print("索引号:", index, "值:", item)
