#write a program to find out whether the file is identical
#and matches the content of another file
file1='copy.txt'
file2='another.txt'

with open(file1) as f:
    f1=f.read()
    with open(file2) as f:
     f2=f.read()

if f1==f2:
    print("files are identical")
else:
    print("files are not identical")