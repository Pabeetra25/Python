#program to find line number where python is present from ques6(in log file)
content="True"
i=1
with open("log.txt") as f:
    
    while content:
       
        content=f.readline()
        

        if 'python' in content.lower():
         print (content)
         print(f"yes,python is present on line number: {i}")
         
        i=i+1
    
