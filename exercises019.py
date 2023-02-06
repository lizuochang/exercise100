# -*- coding:UTF-8 -*-

# python100道经典练习题
# author forever like
"""
 【程序19】
题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程
　　　找出1000以内的所有完数。
"""


def main():

    for i in range(1,1000):
        sum = 0
        for j in range(1,i):
            if i%j==0:
                sum+=j
        if sum==i:
            print("%d,"%i,end="")



if __name__ == '__main__':
    main()
