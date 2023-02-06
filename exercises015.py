# python100道经典练习题
# author forever like
"""
【程序15】
题目：利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

"""
# -*- coding: UTF-8 -*-

def main():
    try:
        number=int(input("Enter a number:"))
    except BaseException:
        print("Plase enter a number!")
    else:
        if number>=90:
            grade="A"
        elif number>=60:
            grade="B"
        else:
            grade="C"
        print(grade)

if __name__=="__main__":
    main()
