from secrets import randbelow


a=[3,5,6,4,7,8,4,56,33,2,8,9,1234,56,77,44]
# b=[]
# for item in a:
#     if item%2==0:
#         b.append(item)
# print(b)
#shortcut code of above
b=[i for i in a if i%2==0]
print(b)        

r=[1,2,3,4,2,3,1,5,3,4,3,2,4]
u={i for i in r}
print(u)