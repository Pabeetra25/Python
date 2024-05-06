#program to find greatest number among three using function
# def greatest(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>a and b>c:
#          return b
#     else:
#         return c

# gr=greatest(44,5,6)
# print("the greatest number is: " + str(gr))
    
def max(num1,num2,num3):
    if(num1>num2):
        if(num1>num3):
            return num1
        else:
            return num3
    else:
        if(num2>num3):
            return num2
        else:
            return num3
m=max(45,33,78)
print("the value of the maximum is " + str(m))                           
