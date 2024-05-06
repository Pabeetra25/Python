x=[1,2,'sun']
len=0
i=0
try:
    while x[i]:
     len+=i
     i+=1
except IndexError:    
    print(len)    