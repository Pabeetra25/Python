from functools import reduce
sum=lambda a,b: a+b
l=[11,12,13,14]
value=reduce(sum,l)
print(value)