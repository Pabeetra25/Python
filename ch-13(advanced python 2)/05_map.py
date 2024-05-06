def square(num):
    return num*num

l=[3,4,5]

#method 1
l2=[]
for item in l:
    l2.append(square(item))
print(l2)

#method 2
print(list(map(square,l)))

#for cube
# def cube(num):
#     return num*num*num

# l=[3,4,5]
# print(list(map(cube,l)))