"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 8:18
# @Author  : Love forever
# @FileName: exercises052.py
# @Software: PyCharm
# @Cnblogs ：
===========================
"""
"""
题目：学习使用按位或 | 。

程序分析：0|0=0; 0|1=1; 1|0=1; 1|1=1

"""
# !/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    a = 0o77
    b = a | 3
    print('a | b is %d' % b)
    b |= 7
    print('a | b is %d' % b)