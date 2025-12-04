f=open("another.txt",'r')
#read first line
text=f.readline()
print(text)
#read second  line
text=f.readline()
print(text)
#read third  line  and so on
text=f.readline()
print(text)

f.close()