# -*- coding: UTF-8 -*-
#@Time : 2022/1/5 8:44
#@File : exercises024.py
#@Software:PyCharm

"""
   【程序24】
   题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""
# def general_term_formula(i):
#     if i<3:
#         result=i
#     else:
#         result=general_term_formula(i-2)+general_term_formula(i-1)
#     return result
#
# sum=0.0
# for i in range(1,21):
#     sum+=(general_term_formula(i+1)/general_term_formula(i))
# print("%f"%sum)

# u = 2.0
# d = 1.0
# s = 0.0
# for i in range(0,20):
#     s = s+u/d
#     u = u+d
#     d = u-d
# print ('%f'%s)