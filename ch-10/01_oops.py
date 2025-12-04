# a=33
# c=32
# print(f"the sum of {a} and {c} is: ",a+c)
class number:
    def sum(self):
        return self.a+self.b
num=number()
num.a=12
num.b=45
s=num.sum()
print(f"the sum is:",s)