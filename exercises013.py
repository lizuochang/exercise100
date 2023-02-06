#python100道经典练习题
#author forever like
"""
程序13：打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。
       例如：153是一个“水仙花数”，因为153=1的三次方＋5的三次方＋3的三次方。
"""
# -*- coding: UTF-8 -*-

def is_narcissistic(number):
    a=number%10
    b=int(number/10)%10
    c=int(number/100)
    return number==a**3+b**3+c**3


if __name__ == "__main__":
    list_temp = []
    for number in range(100, 1000):
        if is_narcissistic(number):
            list_temp.append(number)
    print(list_temp)
