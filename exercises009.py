#python100道经典练习题
#author forever like
"""
程序9：暂停一秒输出。
程序分析：使用 time 模块的 sleep() 函数。
"""
# -*- coding: UTF-8 -*-

import time

myD = {1: 'a', 2: 'b'}
# for key, value in dict.items(myD):
#     print(key, value)
#     time.sleep(1)  # 暂停 1 秒
for key, value in myD.items():
    print(key, value)
    time.sleep(1)  # 暂停 1 秒