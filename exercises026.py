# -*- coding: UTF-8 -*-
#@Time : 2022/1/5 9:33
#@File : exercises026.py
#@Software:PyCharm

"""
   【程序26】
   题目：利用递归方法求5!。
"""

def factorial(i):
    if i == 1:
        return 1
    else:
        return (i * factorial(i - 1))
print (factorial(5))