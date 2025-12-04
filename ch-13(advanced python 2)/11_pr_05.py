'''program to find maximum of the number in a list using
reduce function'''

from functools import reduce
l=[2,34,56,7,8,98]

a=reduce(max,l)
print(a)