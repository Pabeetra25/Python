def greater_than_8(num):
    if num>8:
        return True
    else:
        return False
g50=lambda num:num>50
l=[5,8,98,34,25,2,34,54,10,22,11,1,2,3]
print(list(filter(greater_than_8,l)))
print(list(filter(g50,l)))

