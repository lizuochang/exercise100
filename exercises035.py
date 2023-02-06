# -*- coding: UTF-8 -*-
#@Time : 2022/1/11 16:35
#@File : exercises035.py
#@Software:PyCharm

'''
 演示lambda的使用。
'''
MAXIMUM = lambda x,y :  (x > y) * x + (x < y) * y
MINIMUM = lambda x,y :  (x > y) * y + (x < y) * x

if __name__ == '__main__':
    a = 10
    b = 20
    print ('The largar one is %d' % MAXIMUM(a,b))
    print ('The lower one is %d' % MINIMUM(a,b))