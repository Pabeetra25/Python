class person:
    country="Nigeria"

    def takeWork():
        print("I am working..")

class Employee(person):
    company="Honda"

    def getSalary(self):
        print(f"salary is {self.salary}")   

    def  takeWork(self): 
        print("I am employee and i am working...")   

class programmer(Employee) :
    company="Fiveer"

    def getsalary(self):
        print(f"no salary to programmers")

p=person()

e=Employee()
e.takeWork()
pr=programmer()
print(pr.company)
print(p.country)


