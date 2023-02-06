# -*- coding:UTF-8 -*-

# python100道经典练习题
# author forever like
"""
【程序18】
题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加有键盘控制。

"""

import string


def main():
    int_basis = int(input("input a basis number："))
    int_longest = int(input("input a longest length of number："))
    int_sum = 0
    for i in range(int_longest):
        int_sum = int_sum * 10 + int_basis
        if i == int_longest - 1:
            print("%d" % int_sum, end="")
        else:
            print("%d+" % int_sum, end="")

    print("=%d" % int_sum)


if __name__ == '__main__':
    main()
