"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 17:37
# @Author  : Love forever
# @FileName: exercises045.py
# @Software: PyCharm
# @Cnblogs ：
===========================
"""
"""
题目：统计 1 到 100 之和。

程序分析：无
"""

# !/usr/bin/python
# -*- coding: UTF-8 -*-

tmp = 0
for i in range(1, 101):
    tmp += i
print('The sum is %d' % tmp)