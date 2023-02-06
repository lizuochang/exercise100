# -*- coding: UTF-8 -*-
#@Time : 2022/1/7 14:27
#@File : exercises029.py
#@Software:PyCharm

"""
  【程序30】
  题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。　
"""
answer=["Yes","No"]


i=int(input("enter a number(10000-99999):"))
if i<10000 or i>99999:
    print("input error!")
else:
    i=str(i)
    flag=0
    for j in range(0,2):
        if i[j]!=i[4-j]:
            flag=1
    print(answer[flag])