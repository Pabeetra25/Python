class number:
    def __init__(self,num):
        self.num=num

    def __add__(self,num2) :
     print("Lets add:")
     return self.num + num2.num

    def __mul__(self,num2) :
     return self.num * num2.num

    def __sub__(self,num2) :
     return self.num - num2.num

    def __truediv__(self,num2) :
     return self.num / num2.num

    def __floordiv__(self,num2) :
     return self.num // num2.num

        
n1=number(10)
n2=number(3)

sum=n1+n2
print(sum)
mul=n1*n2
print("Lets multiply:")
print(mul)
sub=n1-n2
print("Lets subtract:")
print(sub)
div=n1/n2
print("division operation:")
print(div)
floordiv=n1//n2
print("Lets do floordivide:")
print(floordiv)