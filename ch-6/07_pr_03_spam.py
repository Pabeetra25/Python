'''a spam comment is defined as a text containing following keywords
"make a lot of money","subscribe the channel","click this"
"buy now",write a program to detect these spams'''
from operator import truediv


text=input("enter the text")


if("make a lot of money" in text):
    spam=True
elif("buy now "in text):
    spam=True
elif("subscribe the channel "in text):
    spam=True
elif("click this "in text):
    spam=True
else:
    spam=False

    if(spam):
        print("this text is spam")
    else:
        print("this text is not spam")