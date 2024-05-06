letter='''dear<|NAME|>,
Greeting from xyz coding house.i am happy to tell your selection           
you are selected!
Have a great day ahead!
Thanks and regards
Anthony
date:<|DATE|>
  '''
name=input("enter your Name\n")
date=input("enter your date\n")
letter=letter.replace("<|NAME>|",name)
letter=letter.replace("<|DATE>|",date)
print(letter)
