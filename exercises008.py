#python100道经典练习题
#author never
"""
程序8：输出9*9口决表
"""
for i in range(1,10):
    for j in range(1,10):
         if i==j:
             print("%d*%d=%d"%(j,i,i*j))
             break
         else:
             print("%d*%d=%d"%(j,i,i*j),end=" ")

