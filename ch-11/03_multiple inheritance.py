class Employee:
    company="visa"
    eCode=1234
class Freelancer:
    compnay="fiverr"
    level=0
    def upgradeLevel(self): 
     self.level=self.level+1
class programmer(Employee,Freelancer):
    name="J-hope"


p=programmer()
p.upgradeLevel()
print(p.level)
print(p.company) #output will be 'visa'due to code.no(9)above as( first,Employee than Freelancer)