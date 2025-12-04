'''program to find whether a given user name contains less than 10
 characters or not'''
str = input("Enter your username : ")

if(len(str)<10):
    print("Number of characters in the string is less than 10.")
elif(len(str)==10):
    print("Number of characters in the string is equal to 10.")
else:
    print("Number of character in the string is greater than 10.")