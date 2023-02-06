# -*- coding: UTF-8 -*-
#@Time : 2022/1/7 14:27
#@File : exercises029.py
#@Software:PyCharm

"""
  【程序29】
  题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""
def PrintReverseOrder(i,cnt):
    if i==0:
        print("\n There are %d digit in the number" % cnt)
        return
    print(int(i%10),end="")
    i=int(i/10)
    cnt += 1
    PrintReverseOrder(i,cnt)



i=int(input("enter a number:"))
PrintReverseOrder(i,0)