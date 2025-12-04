class Employee:
    company="google"
    def showDetails(self):
        print("this is an employee")
class programmer(Employee):
    language="Python"
    company="Youtube"

    def getLanguage(self):
        print(f"the language is {self.language}")

    def showDetails(self):
        print("this is a programmer")   

e=Employee()
e.showDetails()
p=programmer()
p.showDetails()
print(p.company)
    