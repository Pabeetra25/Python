'''write a list comphrensions to print the list which contains
the multiplication table of a user enterd number'''
num=int(input("enter the number:"))
table=[num*i for i in range(1,11)]
print(table)