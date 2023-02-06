#python100道经典练习题
#author forever like
"""
程序12：题目：判断101-200之间有多少个素数，并输出所有素数。
"""
# -*- coding: UTF-8 -*-

def is_prime(number):
    if number<2:
        return False
    else:
        for temp in range(2,number):
            if number%temp==0:
                return False
        return True
def list_get_prime(begin,end):
    list_temp=[]
    for number in range(begin,end+1):
        if is_prime(number):
            list_temp.append(number)
    return list_temp
if __name__ == "__main__":
    print(list_get_prime(101,200))



