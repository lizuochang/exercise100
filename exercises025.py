# -*- coding: UTF-8 -*-
#@Time : 2022/1/5 9:13
#@File : exercises025.py
#@Software:PyCharm

"""
   【程序25】
   题目：求1+2!+3!+...+20!的和
"""
sum=0
item=1
for i in range(1,21):
    item*=i
    sum+=item
print (sum)
