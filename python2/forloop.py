#for loop is used to iterate over a sequence,which
#could be a list,tuples,array or a string
x='whitehouse'
for i in x:
    print(i,end="")

for i in range(0,21,2):
 print(i)

#even or not
sum=0
for i in range(0,21):
   if i%2==0:
      sum+=i
      print(sum)
#1
# 12
# 123
# 1234
# 12345
n=int(input("enter any number"))
for p in range(1,n+1):
   for q in range(1,p+1):
      print(q,end="")
print()
    
    

