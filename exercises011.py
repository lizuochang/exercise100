#python100道经典练习题
#author forever like
"""
程序11：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月
　　　 后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
"""
# -*- coding: UTF-8 -*-

def sumRabbit(month):
    return 2 if month<=2 else sumRabbit(month-1)+sumRabbit(month-2)


if __name__ == "__main__":
    month = int(input("请输入month："))
for i in range(1, month):
    print(i,"->",sumRabbit(i))
