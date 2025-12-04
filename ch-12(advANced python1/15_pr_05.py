'''store the multiplication table generted in problem 3 in a file name
tables.txt'''

num=int(input("enter the number:"))
table=[num*i for i in range(1,11)]
print(table)
with open("tables.txt","a")as f:
    f.write(str(table))
    f.write("\n")