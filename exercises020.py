# -*- coding:UTF-8 -*-

# python100道经典练习题
# author forever like
"""
【程序20】
 题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
      第10次落地时，共经过多少米？第10次反弹多高？
"""


def main():

    # float_hight=100
    # float_sum=0
    # for i in range(1, 11):
    #     float_sum += float_hight*1.5
    #     float_hight /= 2
    # print("hight:%f" % float_hight)
    # print("sum:%f"  % float_sum)
    s = 100.
    h = 50.0
    for i in range(2, 11):
        s += 2 * h
        h /= 2

    print("the sum length of path:%f" % s)
    print("the last height is:%f" % h)

if __name__ == '__main__':
    main()
