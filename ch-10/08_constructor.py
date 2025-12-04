class Employee:
    company='Twitter'
    def __init__(self,name,salary,subunit):
        self.name=name
        self.salary=salary
        self.subunit=subunit
        print("Employee is created")
  
    def getDetails(self):
       print(f"the name of employee is :{self.name}")
       print(f"the salary of employee is :{self.salary}")
       print(f"the subunit of employee is: {self.subunit}")
    def getsalary(self,signature):
       print(f"salary for the people working in {self.company} is {self.salary}\n{signature}")
    @staticmethod
    def greet():
       print("Good morning,sir")

    @staticmethod
    def time():
       print("time is 11:49 pm")

david=Employee("David",3400,"Youtube")
#david=Employee() #throws an error as
# as: Employee.__init__() missing 3 required positional arguments: 'name', 'salary', and 'subunit'
david.getDetails()
''' output:First line print because of _init _ function
And other three lines are printed by getDetails function'''