'''program to find out whether the student is pass or fail
if it requires totL 40% and at least 33%,in each subject
to pass.assume 3 sub and take marks as an input from users'''

sub1=int(input("marks of subject 1:\n"))
sub2=int(input("marks of subject 2:\n"))
sub3=int(input("marks of subject 3:\n"))

if(sub1<33 or sub2<33 or sub3<33):
    print("you are fail because you have got <33 % in one of the subjects ")

elif((sub1+sub2+sub3)/3<40):
    print("you are fail due to total percentage less than 40%")
else:
    print("Congratulations!You are passed in exam")