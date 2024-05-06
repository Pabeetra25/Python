try: 
    q=int(input("enter the number:"))
    a=1/q
    print(a)
except Exception as e:
    print("exception has occured! Try again to enter valid number")
    print(e)
else:
    print("your code run successfully!")