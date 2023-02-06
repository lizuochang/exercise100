"""
============================
# -*- coding: utf-8 -*-
# @Time    : 2023/2/6 17:07
# @Author  : Love forever
# @FileName: exercises041.py
# @Software: PyCharm
# @Cnblogs ：
===========================
"""
"""
题目：模仿静态变量的用法。

程序分析：无。
"""
#!/usr/bin/python
# -*- coding: UTF-8 -*-

def varfunc():
    var = 0
    print ('var = %d' % var)
    var += 1
if __name__ == '__main__':
    for i in range(3):
        varfunc()

# 类的属性
# 作为类的一个属性吧
class Static:
    StaticVar = 5   #静态变量，不需要显示的声明Python中，静态成员变量称为类变量，非静态成员变量称为实例变量
    def varfunc(self):
        self.StaticVar += 1
        print (self.StaticVar)

print (Static.StaticVar)
a = Static()
for i in range(3):
    a.varfunc()