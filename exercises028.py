# -*- coding: UTF-8 -*-
#@Time : 2022/1/6 7:28
#@File : exercises027.py
#@Software:PyCharm


'''
 【程序28】
 题目：有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第
 　　　3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后
 　　　问第一个人，他说是10岁。请问第五个人多大？
 '''
def fun(i):
     if i==1:
         return 10
     return fun(i-1)+2

print(fun(5)) 