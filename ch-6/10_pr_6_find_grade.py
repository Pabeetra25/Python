'''calculate the garade of the students from his marks
      90-100=excleent
      80-90=A
      70-80=B
      60-70=C
      50-60=D
      <50=F'''
marks=int(input("enter yours marks:\n"))

if marks>=90:
    grade="Ex"
elif marks>=80:
     grade="A"  
elif marks>=70:
     grade="B" 
elif marks>=60:
     grade="C" 
elif marks>=50:
     grade="D" 
else:
     grade="F"

print("your grade is "+ grade) 