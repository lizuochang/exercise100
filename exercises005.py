#python100道经典练习题
#author never
"""
程序5：输入三个整数，x,y,z,请把这个数由小到大输出
"""
x = int(input("请输入整数x:"))
y = int(input("请输入整数y:"))
z = int(input("请输入整数z:"))
list_temp = [x, y, z]
for i in range(len(list_temp)-1):
    for j in range(i+1,len(list_temp)):
        if list_temp[i]>list_temp[j]:
            list_temp[i],list_temp[j]=list_temp[j],list_temp[i]
print(list_temp)
