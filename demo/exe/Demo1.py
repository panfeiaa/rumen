"""
1、理解函数：函数是代码的一次封装，是模块化的基础
2、main：函数的入口
    建明思义 ，变量和函数命名都小写  函数命名（动词+名词）
3、写好注释

"""
# 引入模块,分为引入文件和引入文件里的函数，如果引入函数了则不需要模块作为前缀调用
# 代码目录要marked directory as source root，这样不用全路径就可以识别模块

from util import round1

if __name__ == '__main__':
    # 提醒输入圆的半径
    myround = round1.Round()
    print("周长：", myround.circumference)
    print("面积：", myround.area)
