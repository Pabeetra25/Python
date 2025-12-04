#write a program to make copy of the text file"this.txt"
with open("another.txt") as f:
    content=f.read()

with open("copy.txt",'w') as f:
    f.write(content)