#a class is a blueprint for similar objects
class person:
  def __init__(self) -> None:
  
    
      self.name='gfuh'
      self.gender='female'
      self.age=23

  def talk(self):
     print("hi me",self.name)

  def vote(self):
      if self.age<18:
        print("i am not eligible to vote")
      else:
        print("eligible to vote")
obj=person()
person.talk(obj)
person.vote(obj)    
