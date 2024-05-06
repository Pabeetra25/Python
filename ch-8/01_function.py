#program to print percantages of the student from the given marks
# marks1=[56,98,78,65,88]
# percentage1=(sum(marks1)/500)*100

# marks2=[65,89,87,56,81]
# percentage2=((marks2[0]+marks2[1]+marks2[2]+marks2[3]+marks2[4])/500)*100

# print(percentage1,percentage2)


#using function
def percent(marks):
    p=((marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/500)*100
    return p
marks1=[56,98,78,65,88]
percentage1=percent(marks1)
marks2=[65,89,87,56,81]
percentage2=percent(marks2)

print(percentage1,percentage2)
