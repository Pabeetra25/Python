from operator import truediv


a=3
f=4
#arithmetic operators
print("the value of 3+4 is",3+4)
print("the value of 3-4 is",3-4)
print("the value of 3*4 is",3*4)
print("the value of 3/4 is",3/4)
#assignments operators
g=3
g+=2
g-=1
g*=7
print(g)
#comparison operators :returns boolean means 'true' or 'false'
# a=(4>10)
# a=(4>=10)
# a=(4<10)
# a=(4<=10)
a=(4!=10)
print(a)
#logical operators
bool1=True
bool2=False
print("the value of bool1 and bool2 is",(bool1 and bool2))
print("the value of bool1 and bool2 is",(bool1 or bool2))
print("the value of bool1 and bool2 is",(not bool2))