'''can you change the self parameter inside a class to something else
(say'Roman' . try changin 'self' to 'slf' or 'Roman' and see the effects'''
 
from unicodedata import name


class sample:
    
    def __init__(slf,name):
        slf.name=name


obj=sample("Roman")  #creating object


print(obj.name)
