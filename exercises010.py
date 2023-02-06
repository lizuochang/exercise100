#python100道经典练习题
#author forever like
"""
程序10：暂停一秒输出，并格式化当前时间。
程序分析：使用 time 模块的 sleep() 函数。
"""
# -*- coding: UTF-8 -*-

import time

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

# 暂停一秒
time.sleep(1)

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))