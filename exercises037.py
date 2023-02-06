# -*- coding: UTF-8 -*-
#@Time : 2022/1/29 22:04
#@File : exercises037.py
#@Software:PyCharm
# author : Love forever

"""
题目：按逗号分隔列表。
程序分析：无。
"""

L = [1, 2, 3, 4, 5]
s1 = ','.join(str(n) for n in L)
print(s1)