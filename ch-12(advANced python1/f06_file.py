from optparse import make_option
from threading import main_thread
from pip import main


def greet(name):
    print(f"Good Morning! {name}")

#print(__name__)
if __name__ =="__ main__":
   n=input("enter the name:\n")    
   greet(n)