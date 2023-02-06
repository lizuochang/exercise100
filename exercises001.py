"""
【程序1】
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
"""
# cnt=0 #count the sum of result
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and j!=k and k!=i:
#                 print(i*100+j*10+k)
#                 cnt+=1
# print(cnt)

# cnt=0 #count the sum of result
# list_number=list()
# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if i!=j and j!=k and k!=i:
#                 list_number.append(i*100+j*10+k)
#                 cnt+=1
# print("符合要求的三位数共%d个！"%cnt)
# print(list_number)
num=0
list_temp=[]
for j in range(1,5):
    for i in range(1,5):
        if j!=i:
            num+=1
            list_temp.append(j*10+i)
print("符合要求的数有%d个！"%num,"它们是：",list_temp)
