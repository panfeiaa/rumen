"""
while循环案例
随机获取50-100内10个互不相等的10个数
"""
import random


# 方式1：通过判断和字典存储数据和打印信息来校验参数生成数据
def get_numbers(start: int, end: int, number: int):
    """
    获取一定范围内互不相等的一定数量的值
    :param start:范围的起始值
    :param end:范围的结束值
    :param number:获取的数量
    :return:返回集合
    """
    # 定义一个集合
    # numbers = []
    # 定义一个字典存储结果
    results = {"data": [], 'info': ""}
    if end - start < number:
        results['info'] = "提供数字范围过小，不符合要求"
        # 开始循环,数量没控制用while
        return results
    else:
        while True:
            # 获取一个随机数,randint是右闭区间，randrange是右开区间获取
            temp = random.randint(start, end)
            # 判断集合里是都有这个值
            if temp not in results["data"]:
                results["data"].append(temp)
            # 判断数量是否达到要求
            if len(results["data"]) == number:
                break
        return results


# 方式1：通过异常机制判断参数
def get_numbers1(start: int, end: int, number: int):
    """
    获取一定范围内互不相等的一定数量的值
    :param start:范围的起始值
    :param end:范围的结束值
    :param number:获取的数量
    :return:返回集合
    """
    # 定义一个集合
    numbers = []
    # 定义一个字典存储结果
    if end - start < number:
        raise Exception('提供数字范围过小，不符合要求')

    while True:
        # 获取一个随机数,randint是右闭区间，randrange是右开区间获取
        temp = random.randint(start, end)
        # 判断集合里是都有这个值
        if temp not in numbers:
            numbers.append(temp)
        # 判断数量是否达到要求
        if len(numbers) == number:
            break
    return numbers


if __name__ == '__main__':
    """
    # 方法1
    result = get_numbers(11, 100, 100)
    if len(result['info']) == 0:
        print("获取的集合为： ", result['data'])
    else:
        print(result['info'])    
    """
    try:
        list01 = get_numbers1(50, 100, 10)
        print("获取的集合为：", list01)
    except Exception as e:
        print(str(e))





