# -*- coding: UTF-8 -*-
#@Time : 2022/1/10 10:12
#@File : exercises033.py
#@Software:PyCharm

'''
  【程序33】
  题目：求一个3*3矩阵对角线元素之和
'''
l = []
for i in range(3):
    for j in range(3):
        l.append(int(input('Input a number:')))
s = 0
for i in range(3):
    s += l[3 * i + i]
print(s)
