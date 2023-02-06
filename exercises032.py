# -*- coding: UTF-8 -*-
#@Time : 2022/1/8 17:28
#@File : exercises031.py
#@Software:PyCharm
"""
【程序37】
 题目：对10个数进行排序
"""
print("input ten numbers please:")
list_num=[]
for i in range(10):
    list_num.append(int(input("enter a number:")))
#可以直接使用sort函数：l.sort()
#也可以自己写排序代码(选择排序)
list_num.sort()
print(list_num)
list_num.sort(reverse=True)
print(list_num)