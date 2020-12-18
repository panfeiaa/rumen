"""
for循环案例

"""

import time


def get_sum01(start: int, end: int):
    sums = 0
    for i in range(start, end + 1, 1):  # [10, 20)开区间
        sums += i
    return sums


def get_sum02(list01: list):
    sums = 0
    for i in list01:
        sums += i
    return sums


def get_numbers01(start: int, end: int, number: int):
    """
    获取一个范围内，某个值所有倍数的值集合
    :param end:
    :param number:
    :param start:
    :return:
    """
    numbers = []
    for i in range(start, end + 1):
        if i % number == 0:
            numbers.append(i)
    return numbers


def get_numbers02(start: int, end: int, number: int):
    numbers = []
    one_number = 0
    if (start <= number <= end) is False:
        raise Exception('数据超出给的数据范围！')
    for i in range(start, end+1):
        if i % number == 0:
            one_number = i
            break
    for i in range(one_number, end, number):  # 使用第一次查到的倍数值为起始值，用除数本身做为步长大幅提高效率
        if i % number == 0:
            numbers.append(i)
    return numbers


if __name__ == '__main__':
    # 求两个数的范围内数据之和(10, 20)
    start1 = 12345678
    end1 = 87654321
    number1 = 13572468
    t1 = time.time()
#    rs01 = get_numbers01(start1, end1, number1)
    t2 = time.time()
#    print("方法1结果:", rs01)
    print("方法1执行时间：", t2 - t1)
    t3 = time.time()
    try:
        rs02 = get_numbers02(start1, end1, number1)
        print("方法2结果:", rs02)
    except Exception as e:
        print(str(e))
    t4 = time.time()
    print("方法2执行时间：", t4 - t3)
