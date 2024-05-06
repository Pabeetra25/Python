# program to read the text from given file"poem.txt"
#and find out whether it contains the word 'twinkle'or not
f=open('poems.txt')
t=f.read()
if 'twinkle' in t:
    print("twinkle is present in the poems")
else:
 print("not present")
f.close()