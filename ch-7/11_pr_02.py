#program to greet all the persons names stored in a list l1 &
# WHICH STARTS WITH 'S'
# l1=['suraj','sant','shyam','ruby']
l1=['suraj','sant','shyam','ruby']
for name in l1:
    if name.startswith("s"):
        print("Hello!" + name)
