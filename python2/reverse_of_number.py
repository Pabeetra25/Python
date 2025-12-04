n=int(input("enter the number"))
r=0
while n%10!=0:
    c=n%10
    r=r*10+c
    n=n//10
print(r)