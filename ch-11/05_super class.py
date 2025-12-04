class person:
    country="Nigeria"

    def __init__(self):
        print("Initializing Person...\n")

    def getWork(self):
        
        print("I am working to earn money..")

class Employee(person):
    company="Honda"
    
    def __init__(self):
        super().__init__()
        print("Initializing Employee...\n")

    def getSalary(self):
        print(f"salary is {self.salary}")   

    def  getWork(self): 
        super().getWork()
        print("I am employee and i am working...")   

class programmer(Employee) :
    company="Fiveer"
     

    def __init__(self):
        super().__init__()
        print("Initializing programmer...\n")
    def getsalary(self):
       print(f"no salary to programmers")

    def getWork(self): 
        super().getWork()
        print("I am employee and i have to work hard so much")

# p=person()
# p.getWork()
# e=Employee()
# e.getWork()
pr=programmer()
# pr.getWork()



