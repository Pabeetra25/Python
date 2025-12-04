'''create a class programmer for storing information of few
 programmers working at microsoft'''
class programmer:
    company="google"
    def __init__(self,name,product) :
        self.name=name
        self.product=product
    def getinfo(self):
        print(f"the name of the {self.company} programmeer is  {self.name} and the product is  {self.product}")
        
simon=programmer("Simon",'Github')       
seema=programmer("seema",'skype')
simon.getinfo()
seema.getinfo()