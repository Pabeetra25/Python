#list-collection of data which can hold values of multiple data types

#1creating list
num=[2,4,5,6]
print(num)
letter=['a','g','o','g','k']
print(letter)
stg=['man','waba','laagw','swaree','dil']
print(stg)
mix=[1,'d','sarbina',3]
print(mix)
#2accessing elememts in list
print(mix[::2])
print(mix[::-1])
print(mix[1::2])

#operation on list
z=[0]*100
print(z)
conc=letter+stg
print(conc)

var=list("hello people")
print(var)

print(num)
one,*other=num
print(one)
print(other)

#methods in list
num.append(11)
print(num)
num.extend(stg)
print(num)
num.insert(2,'gagan')
print(num)
num.remove("swaree")
print(num)

var1=['n','i','h','c','a','s']
var1.sort()
print(var1)

#built-in-function with list
w=[1,2,3,4,5,6,7,8,9]
print(len(w))
print(max(w))
print(min(w))
print(sum(w))
print(sum(w)/len(w))