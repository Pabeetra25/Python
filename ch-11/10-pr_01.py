'''create a class C2d vector and use it create another class 
representing a 3d vector '''
class c2dvec:
    def __init__(self,i,j):
        self.icap=i
        self.jcap=j
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j"

class c3dvec(c2dvec):
    def __init__(self,i,j,k):
        super(). __init__(i,j)
        self.kcap=k
    def __str__(self):
        return f"{self.icap}i+{self.jcap}j+{self.kcap}k"

v2d=c2dvec(2,3)
v3d=c3dvec(4,5,6)
print("2D vector is expressed as:",v2d)
print("3D vector is expressed as :",v3d)