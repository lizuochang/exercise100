# -*- coding: UTF-8 -*-
#@Time : 2022/1/11 16:10
#@File : exercises034.py
#@Software:PyCharm

"""
  【程序34】
   题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
"""
list_num = [0,10,20,30,40,50]

print("The sorted list is",list_num)
count=len(list_num)
num=int(input("enter a number:"))
list_num.append(num)
for i in range(count):
    if num<list_num[i]:
        for j in range(count,i,-1):
            list_num[j],list_num[j-1]=list_num[j-1],list_num[j]
        break
print("The new sorted list is",list_num)
