"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 15:39
# @Author  : Love forever
# @FileName: exercises066.py
# @Software: PyCharm
# @Cnblogs ：
===========================
"""
"""
题目：输入3个数a,b,c，按大小顺序输出。　　　

程序分析：无。
"""
# !/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    n1 = int(input('n1 = :\n'))
    n2 = int(input('n2 = :\n'))
    n3 = int(input('n3 = :\n'))


    def swap(p1, p2):
        return p2, p1


    if n1 > n2: n1, n2 = swap(n1, n2)
    if n1 > n3: n1, n3 = swap(n1, n3)
    if n2 > n3: n2, n3 = swap(n2, n3)

    print("%d,%d,%d"%(n1,n2,n3))