'''program to display a/b where a and b are integers
if b=0,display infinite by handling the zerodivision error'''

a=int(input("enter number a:\n"))
b=int(input("enter number b:\n"))

try:
    print(a/b)

except:
    print("infinite")    