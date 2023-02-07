"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 8:16
# @Author  : Love forever
# @FileName: exercises051.py
# @Software: PyCharm
# @Cnblogs ：
===========================
"""
"""
题目：学习使用按位与 & 。

程序分析：0&0=0; 0&1=0; 1&0=0; 1&1=1。
"""
# !/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    a = 0x77
    b = a & 3
    print('a & b = %d' % (a & b))
    b &= 7
    print('a & b = %d' % (a & b))