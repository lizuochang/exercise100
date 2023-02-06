#coding=utf-8

"""
   【程序23】
   题目：打印出如下图案（菱形）

      *
     ***
    *****
   *******
    *****
     ***
      *
"""

for i in range(1,8,2):
    print(" "*int((7-i)/2)+"*"*i)
for i in range(5,0,-2):
    print(" "*int((7-i)/2)+"*"*i)