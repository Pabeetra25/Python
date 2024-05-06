class Employee:
  company="Nepail ol corporation"
  salary=30000
  salarybonus=1200
  
  @property
  def totalsalary(self):
      return self.salary+self.salarybonus
   
  @totalsalary.setter
  def totalsalary(self,value):
      self.salarybonus=value-self.salary
e=Employee()
print(e.totalsalary)
e.totalsalary=32000
print(e.salary)
print(e.salarybonus)