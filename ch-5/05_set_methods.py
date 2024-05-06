#creating an empty set
c=set()
print(type(c))
#adding values to an empty set
c.add(4)
c.add(8)#adding the value repetedly doesn't changes the set
c.add(8)
c.add((2,3,4,5))
#c.add({3:4})#can't add list or dictionary to sets
print(c)
print(len(c))#print the length of the set
#removal of items from sets
c.remove(8)#removes 8 from set c
#c.remove(12)#throws an error(as 12 is not present in the set c)
print(c)
print(c.pop())
print(c)