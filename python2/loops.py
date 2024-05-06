#while loops
val=int(input("enter number multiple of 7"))
while val%7!=0:
    val=int(input("enter number multiple of 7"))
else:
    print("%d is the multiple of 7 "%val)   

#for loop
a=[3,4,'sample']
for i in a:
    print(i)      

x=[[1,2,3],['a','b','c']]  
for i in x:
    for j in i:
        print(j , end=" ")  
       
#break statement
a="hello there,i am here"
for i in a:
    if i==",":
        break
    print(i, end="")  

#continue statement
v=[1,2,3,4,5,6]
for i in v:
    if i==4:
        continue
    print(i)