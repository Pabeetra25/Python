#factorial of a number
def factorial(n):
 if n==0 or n==1:
  return 1
 else:
  return n*factorial(n-1)  
p=factorial(5) 
print("factorial is",p) 