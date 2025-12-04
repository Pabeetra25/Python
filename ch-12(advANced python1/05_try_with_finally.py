try: 
    q=int(input("enter the number:"))
    a=1/q
    print(a)
except Exception as e:
    print("exception has occured! Try again to enter valid number")
    print(e)
    exit()
finally:
    print("your are done!")