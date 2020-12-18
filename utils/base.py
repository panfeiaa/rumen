# 常量要大写
PI = 3.1415926
def check_radius():
    """
    终端输入的半径，如果不符合要求，提醒重新输入，如果符合要求，直接返回
    :return:
    """
    # 使用异常处理，如果不符合要求，出现异常，重新输入
    # 如何保证翻覆输入，必须要使用循环，while（次数不明确）和for循环
    while True:
        # 提醒输入半径
        input_str = input("请输入圆的半径：")
        # 异常处理 ： try(有可能出现异常的代码) ——————》except （出现异常的处理代码）
        try:
            radius = float(input_str)
            return radius
        except:
            print("输入的半径不符合要求")


def get_circumference(self):
    """
    获取圆的周长
    :param radius:提供的半径
    :return: 返回周长值
    """
    return 2 * PI * self.radius


def get_area(self):
    """
    获取圆的面积
    :param radius:提供的半径
    :return: 返回圆的面积
    """
    return PI * self.radius * self.radius