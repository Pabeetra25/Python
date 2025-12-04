#print multiplication table of a nuber in reverse order
num=int(input("enter the number:\n"))

for i in reversed (range(1,11)):
   print(f"{num}*{i}={num*i}")
 