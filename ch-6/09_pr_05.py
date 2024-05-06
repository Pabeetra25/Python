# str=input("enter username")
# if(len(str)<10):
#     print("<10 characters")
# elif(len(str)==10):
#     print("10 characters")
# else:
#     print("> characters")


#program which finds out whether the given name is present in the list or not
names=["namjoon","jin","j-hpoe","kookie","jimin","suga","tehyung"]
name=input("enter the name to check:\n")

if name in names:
    print("name is present in the list")
else:
    print("name is  notpresent in the list")