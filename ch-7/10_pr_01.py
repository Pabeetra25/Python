#program to print multiplication table of given nuber using for loop
num=int(input("enter the number"))
for i in range(1,11):
   # print(str(num) + "x" + str(i) +"=" + str(i*num))
    print(f"{num}x{i}={num*i}")
