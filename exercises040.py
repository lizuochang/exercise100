"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 16:33
# @Author  : Love forever
# @FileName: exercises040.py
# @Software: PyCharm
# @Cnblogs ：
===========================
"""
"""
题目：将一个数组逆序输出。

程序分析：用第一个与最后一个交换。
"""
def main():
    a = [9, 6, 5, 4, 1]
    b=a[::-1]
    print(b)
    print(a)
    # N=len(a)
    # for i in range(N//2):
    #     a[i],a[N-1-i]=a[N-1-i],a[i]
    # print(a)
if __name__ == '__main__':
    main()