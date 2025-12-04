'''create a class with class attributes 'a' ;create an object from it and
set a directly using object.a=0
Does this change class attributes'''

class name:
    a="Dyanel"

obj=name()  #creating object
obj.a="Zuckerberg"
#name.a="xexexe"  #this code replace the name of 'dyanel' to 'xexexe'

print(name.a)
print(obj.a)