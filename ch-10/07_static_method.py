class Employee:
    company='Twitter'
   
    def getsalary(self,signature):
        print(f"salary for the people working in {self.company} is {self.salary}\n{signature}")
    @staticmethod
    def greet():
     print("Good morning,sir")

    @staticmethod
    def time():
     print("time is 11:49 pm")
prince=Employee()
prince.salary=200000
prince.getsalary("Thanks!")  #or..Employee.getsalary(prince)
prince.greet() #Employee.greet()
prince.time()