'''create a class employee and add salary and increment properties
to it. write a method salaryafterincrement with a @property decorator
with a setter which changes the value of increment based on the salary'''

class Employee:
    salary=2500
    increment=1.5

    @property
    def salaryAfterIncrement(self):
        return self.salary*self.increment

    @salaryAfterIncrement.setter
    def salaryAfterIncrement(self,sai):
     self.increment=sai/self.salary 


e=Employee()
print(e.salaryAfterIncrement)
print(e.increment)
e.salaryAfterIncrement=4000
print(e.increment)