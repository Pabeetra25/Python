#program to find sum of first n natural numbers using while loop
from re import I


num = int(input("enter the number: "))

i = 1 
sum = 0
while (i<=num):
 sum =sum+i
i=i+1
print(f"The sum of first {num} natural number is {sum}")