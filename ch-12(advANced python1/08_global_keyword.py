s=89  #global variable
def num():
    global s
    print(f"print statement1: {s}")
    s=67 #Local variable if global keyword is not used
    print(f"print statement2: {s}")
num()    
print(f"print statement3: {s}")