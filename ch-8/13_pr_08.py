#python function to print multiplication table of a given number
# num=int(input("enter the number:"))
# print("multiplication table of:",num)
# for i in range(1,11):

#  print(num,'X',i,'=',num*i)

def print_mul_table(num): 
    
 for i in range(1,11): 
  print(num,' x ',i,' = ',num*i) 

n = int(input(" Enter a number:"))
print_mul_table(n)
