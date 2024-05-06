class Employee:
    company="google"

Scarleet=Employee()
Zendya=Employee()
Scarleet.salary=45000
Zendya.salary=87000
print(Scarleet.company)
print(Zendya.company)
Employee.company="microsoft"
print(Scarleet.company)
print(Zendya.company)
print(Scarleet.salary)
print(Zendya.salary)
