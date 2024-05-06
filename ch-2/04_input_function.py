'''input()function allows the user to take 
input from the keyboard as a string'''
#output of input is always string even if the number is entered
a=input("Enter your name:")
print(a)
print(type(a))
a=input("Enter your location id:")
a=int(a) #convert a to an integer(if possible)
print(a)
print(type(a))