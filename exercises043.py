"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 17:32
# @Author  : Love forever
# @FileName: exercises043.py
# @Software: PyCharm
# @Cnblogs ：
===========================
"""
"""
题目：模仿静态变量(static)另一案例。

程序分析：演示一个python作用域使用方法
"""

#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print ('nNum = %d' % self.nNum)

if __name__ == '__main__':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print ('The num = %d' % nNum)
        inst.inc()