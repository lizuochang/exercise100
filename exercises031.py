# -*- coding: UTF-8 -*-
#@Time : 2022/1/8 17:28
#@File : exercises031.py
#@Software:PyCharm
"""
   【程序31】【筛选法】
   题目：求100之内的素数　　
"""
a=[1]*101
for i in range(2,11):
    for j in range(i*2,101,i):
        a[j]=0
print("prime number is:")
for i in range(2,101):
    if a[i]:
        print(i,end=",")