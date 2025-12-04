'''create a class pets from class animals and further cretate
a class dog from pets.add a method bark to class dog'''
class Animals:
    animalTypes="mammals"

class Pets(Animals):
    color="white"

class Dog(Pets):
    @staticmethod
    def bark():
        print("the dog is barking like  :Baff.. Baff...")

d=Dog()
d.bark()