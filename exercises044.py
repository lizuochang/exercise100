"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 17:35
# @Author  : Love forever
# @FileName: exercises044.py
# @Software: PyCharm
# @Cnblogs ：
===========================
"""

"""
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：
程序分析：创建一个新的 3 行 3 列的矩阵，使用 for 迭代并取出 X 和 Y 矩阵中对应位置的值，相加后放到新矩阵的对应位置中。
"""

# !/usr/bin/python
# -*- coding: UTF-8 -*-

X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# 迭代输出行
for i in range(len(X)):
    # 迭代输出列
    for j in range(len(X[0])):
        result[i][j] = X[i][j] + Y[i][j]

for r in result:
    print(r)