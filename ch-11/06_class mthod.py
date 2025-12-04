class Employee:
    company="Tesla"
    salary=40000
    location="California"

    # def changeSalary(self,sal):
    #  self. __class__ .salary=sal
      
    @classmethod
    def changeSalary(cls,sal):
        cls.salary=sal

e=Employee()
print(e.salary)
e.changeSalary(34430)
print(e.salary)
print(Employee.salary)