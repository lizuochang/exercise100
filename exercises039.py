"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 15:51
# @Author  : Love forever
# @FileName: exercises039.py
# @Software: PyCharm
# @Cnblogs ：
===========================
"""
"""
题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
程序分析：首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入
后此元素之后的数，依次后移一个位置。
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-
def main():
    a = [1, 4, 6, 9, 13, 16, 19, 28, 40, 100]
    number = int(input("\n插入一个数字:\n"))
    for i in range(len(a)):
        if number<=a[i]:
            a.insert(i,number)
            break
    print(a)




if __name__ == '__main__':  #输入main，敲回车即可。
    main()
