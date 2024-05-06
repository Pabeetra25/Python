while(True):
    print("press q to quit")
    a=(input("enter  a number:"))
    if a=='q':
        break
    try:
        print("TRying.....")
        a=int(a)
        if(a>6):
           print("the number is  greater than 6")
    except Exception as e:
        print(e)
        print(f"your input resulted in an error:{e}")
print("Thanks!for playing the game")