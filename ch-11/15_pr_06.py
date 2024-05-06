'''write __str__() method to print the vector as follows
     7i+8J+10k
     assume vector of dimension 3 for this problem'''

class vector:
    def __init__(self,vec):
        self.vec=vec
    def __str__(self):
        return f"{self.vec[0]}i+{self.vec[1]}j+{self.vec[2]}k"
v1=vector([2,4,6])
v2=vector([5,6,8])
print(v1)            
print(v2)        