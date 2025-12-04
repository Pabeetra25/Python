#the perfect guess
import random
randnumber=random.randint(1,100)
# print(randnumber)
userGuess=None
guesses=0
while(userGuess!=randnumber):
    userGuess=int(input("enter your guess:"))
    guesses+=1
    if(userGuess==randnumber):
        print("Finally,you guess the right one")
    else:
        if (userGuess>randnumber):
          print("your guess is higher then actual ones!Enter the smaller one please!")
        else:
           print("you guess is wrong!,enter larger number")
   
print( f"you guess the number in {guesses} guesses")

with open("another.txt","r") as f:
    hiscore=int(f.read())

if(guesses<hiscore):
    print("you have just broken the high score!")

with open("another.txt",'w') as f:
    f.write(str(guesses))    