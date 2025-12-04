try:
    a=int(input("enter a number:"))
    c=1/a
    print(c)

except ValueError as e:
 print("Please Enter the valid value:")
 print(e)

except ZeroDivisionError as e:
 print("Make sure yuo are not dividing by 0")
 print(e) 

print("Thanks for playing game")