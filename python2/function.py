#function-is a set of some code that performs some task
def add(a,b):
    sum=a+b
    print(id(a),id(b))
    print("a:%d  b:%d" %(a,b))
    print("the sum is",sum)
add(3,44)    
x=9
y=8
print(id(x),id(y))
add(x,y)


def add(*a):
    total=0
    for i in a:
        total=total+i
    print("the sum is",total)
add(1,2,3,4,5) 

