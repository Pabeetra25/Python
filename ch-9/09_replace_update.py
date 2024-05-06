'''a files contains a word "election" multiples time.write 
program to replace this word with###### and by updating the 
same file'''
with open("poems.txt") as f:
    c = f.read()

c = c.replace("election", "$%^@$^#^")

with open("poems.txt", "w") as f:
    f.write(c)
