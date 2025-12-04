#dictionary is an unordered collection of data stored as a pair of keys and values
#syntax-variable-name={key:value}

#creating dictionaries
d1={}
print(d1)
print(type(d1))

d2={1:"Nepal",2:'India',3:"China"}
print(d2)

d3={'name':"khim",'age':24,'profession':'soilder'}
print(d3)

#adding element
d={}
d[0]='welcome'
d[1]=("how",'are','you')
d['name']='sam'
print(d)
d['name']={'first':'sam','second':'rana'}
print(d)
#accessing element
print(d['name'])
print(d['name']['first'])
print(d.get(1))
#deleting elements
d.pop(0)
print(d)
d.popitem()
print(d)
#using built-in-functions
print(d.values())

keys={'a','b','c','d'}
value=1
print(dict.fromkeys(keys,value))
d.clear()
print(d)

#set-is an unorderd collection of unique elements
#syntax-variable_name=set(['a','b','c','d'])
s=set([1,2,3,4])
print(s)
print(type(s))
s.add('appke')
print(s)

#frozen set
fs=frozenset([2,3])
print(fs)
# fs.add('a')-->error
s1=set([1,2,3,4])
s2=set([2,3,5,6])
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))