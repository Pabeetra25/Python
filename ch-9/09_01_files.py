#use open() function to read the content of the file
#f = open ('sample.txt' , 'r')
f = open('another.txt') #by default in read mode
data = f.read()
#data = f.read(5)#read first five character from the file
print(data)
f.close()