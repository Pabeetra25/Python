'''program to create a dictionary of nepali words with
values as their english translation'''
#provide user with an option to look it up|
mydic={
    "ghar":"house",
    "mato":"soil",
    "samundra":"ocean",
    "bishow":"world"
}
print("options are ",mydic.keys())
a=input("enter the nepali word\n")
#print("the meaning of your word is:",mydic[a])
#below line will not throw an error if the key is not
#  present in the dictionary
print("the meaning of your word is:",mydic.get(a))