# -*- coding: UTF-8 -*-
#@Time : 2022/1/29 21:34
#@File : exercises036.py
#@Software:PyCharm

"""
【程序36】使用函数，输出三次 RUNOOB 字符串。
程序分析：练习函数调用。
"""


def hello_runoob():
    print('RUNOOB')


def hello_runoobs():
    for i in range(3):
        hello_runoob()


if __name__ == '__main__':
    hello_runoobs()