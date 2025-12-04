#repeat pr4 for a list of such words to be censored
words=['manang','mustang','pokhara']
with open("poems.txt") as f:
    c = f.read()
for word in words:
 c = c.replace(word, "$%^@$^#^")

with open("poems.txt", "w") as f:
    f.write(c)