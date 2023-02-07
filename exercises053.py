"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2023/2/7 8:22
# @Author  : Love forever
# @FileName: exercises053.py
# @Software: PyCharm
# @Cnblogs ：
===========================
"""
"""
题目：学习使用按位异或 ^ 。

程序分析：0^0=0; 0^1=1; 1^0=1; 1^1=0
"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-

if __name__ == '__main__':
    a = 0o77
    b = a ^ 3
    print ('The a ^ 3 = %d' % b)
    b ^= 7
    print ('The a ^ b = %d' % b)