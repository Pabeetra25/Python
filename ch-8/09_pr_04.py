#recursive function to calculate sum of first n natural numbers
def sum(n):
    if(n==1):
        return 1
    else:  
        return n+sum(n-1)
n=18
s=sum(n)
print("the sum is: " + str(s))