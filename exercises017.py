# python100道经典练习题
# author forever like
"""
【程序17】
题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

"""
# -*- coding: UTF-8 -*-

import string

def main():
    str_temp=input("input a string：")
    letter=0
    space=0
    digit=0
    other=0
    for str in str_temp:
        if str.isalnum():
            letter+=1
        elif str.isspace():
            space+=1
        elif str.isdigit():
            digit+=1
        else:
            other+=1
    print('There are %d letters,%d spaces,%d digits and %d other characters in your string.' % (letter, space, digit, other))

if __name__ == '__main__':
    main()

