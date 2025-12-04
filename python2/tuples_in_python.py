#tuple-is a collection of immutable heterogeneous python objects

#creating tuples
a=()
print(type(a))
print(a)

city='ktm','lalitpur','bhaktapur'
print(city)
print(city[2])
print(city[::-1])
c=1,2,3,4
conc=city+c
print(conc)

nest=(city,c)
print(nest)

#repititon
rep=('canada',)
print(rep*5)
#slicing
a=('wahington')
print(a[:])
print(a[3:])
print(a[2:4])

#unpacking
print(tuple('iloveu'))
num=1,2,3,4
print(num)
a,b,c,d=num
print(a,b,c,d)
a,*f,c=num
print(a,f,c)

#built-in-function
t=(1,2,4,5,6,7,33,4,4)
print(t.count(4))
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
print(sum(t)//len(t))

#converting list to tuple
lst=[1,2,5,6]
tup=tuple(lst)
print(tup)
print(type(tup))

#Nesting tuple in a list
lst=[(1,2,3),(4,5,6)]
lst.append(('ser','she','emer'))
print(lst)
lst.remove((1,2,3))
print(lst)

#nesting list within tuples
tup=([1,2,3],[5,6,7])
tup[0].append(5)
print(tup)
tup[1].remove(6)
print(tup)