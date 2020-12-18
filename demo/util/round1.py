"""
本模块实现圆的半径输入，要大写

"""

# 常量要大写
PI = 3.1415926


class Round:
    # 累的构造函数，主要用来初始化类（需要哪些数据，就通过初始化类传递过来）
    # __init__函数实例化的时候自动执行！
    def __init__(self):
        # 使用类的属性接受传递来的值
        self.radius = 0.0
        self.circumference = 0.0
        self.area = 0.0

        self.check_radius()
        self.get_circumference()
        self.get_area()

    def get_circumference(self):
        """
        获取圆的周长
        :return: 返回周长值
        """
        self.circumference = 2 * PI * self.radius

    def get_area(self):
        """
        获取圆的面积
        :return: 返回圆的面积
        """
        self.area = PI * self.radius * self.radius

    def check_radius(self):
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
                self.radius = float(input_str)
                # 终止循环
                break
            except:
                print("输入的半径不符合要求")
