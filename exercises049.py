"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 17:47
# @Author  : Love forever
# @FileName: exercises049.py
# @Software: PyCharm
# @Cnblogs ：
===========================
"""

"""
题目：使用lambda来创建匿名函数。

程序分析：无
"""
# !/usr/bin/python
# -*- coding: UTF-8 -*-

MAXIMUM = lambda x, y: (x > y) * x + (x < y) * y
MINIMUM = lambda x, y: (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print('The largar one is %d' % MAXIMUM(a, b))
    print('The lower one is %d' % MINIMUM(a, b))
