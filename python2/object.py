class person:
    def __init__(self,n,g,a) -> None:
        self.name=n
        self.gender=g
        self.age=a
    def laugh(self):
        print("it's me",self.name )  
    def vote(self):
        if self.age<18:
            print("can't vote")
        else:
            print("can vote") 
obj1= person('sama','female',12)
obj2=person('ram','male',45)
obj1.vote()
obj1.laugh()
obj2.laugh()
obj2.vote() 
