class Employee:
    company='Twitter'
    def getsalary(self):
        print(f"salary for the people working in {self.company} is {self.salary}")
prince=Employee()
prince.salary=200000
prince.getsalary()  #or..Employee.getsalary(prince)