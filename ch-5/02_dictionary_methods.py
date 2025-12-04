dic={
"Elon Musk":"the richest man in the world",
"johhny deep":"the film star",
"marks":[1,4,5] ,
"anotherdic":{'Elon Musk':'owner of Tesla company'},
1:23
}
#dictionary methods
print(dic.items())#print the(key and values for all contents of the dictionary)
print(list(dic.keys()))#prints the keys of the dictionary
print(dic.values())#prints the values of the dictionary
print(dic)
updatedict={
    "largest country":"Russia",
    "smallest country":"vatican city"
    }
dic.update(updatedict)#update the dictionary by adding(key-value)pairs from updatedict

print(dic)
print(dic.get("smallest country"))#print value associated with key-smallest country
print(dic['smallest country'])#print value associated with key-smallest country
#the difference between .get and[]syntax in a dictionary?
print(dic.get("smallest country1"))#returns none as smallest country1 is not present in the dictionary
print(dic['smallest country1'])#throws error as smallest country1 is not present in the dictionary
