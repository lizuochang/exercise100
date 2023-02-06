# python100道经典练习题
# author forever like
"""
程序13：输入一个正整数，分解质因数
"""
# -*- coding: UTF-8 -*-
from typing import List

# number = int(input("请输入一个正整数："))
# list_temp = []
# flag = True
# while flag:
#     for i in range(2, number + 1):
#         if number % i == 0 and number / i!=1:
#             list_temp.append(i)
#             number = int(number / i)
#             break
#
#     if i==number:
#         list_temp.append(i)
#         flag = False
# print(list_temp)

def reduceNum(n):
    print('{} = '.format(n),end="")
    if not isinstance(n,int) or n <= 0:
        print('请输入一个正确的数字 !')
        exit(0)
    elif n in [1] :
        print('{}'.format(n))
    while n not in [1] : # 循环保证递归
        for index in range(2, n + 1):
            if n % index == 0:
                n =int(n/ index) # n 等于 n/index
                if n == 1:
                    print(index)
                else : # index 一定是素数
                    print('{} *'.format(index),end=" ")
                break
reduceNum(90)
reduceNum(100)