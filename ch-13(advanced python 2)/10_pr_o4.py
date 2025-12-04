'''program to filter the list of number divisible by 5'''
#first method
def div_by_5(num):
    if num%5==0:
        return True
    else:
        return False
l=[2,10,15,80,56,70,90,95]

print(list(filter(div_by_5,l)))
#second method
l=[2,10,15,80,56,70,90,95]
a=filter(lambda a:a%5==0,l)
print(list(a))