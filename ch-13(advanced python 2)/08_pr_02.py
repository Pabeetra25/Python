'''program to input company, name,and rank of a billioner
and format it using the format function as below:
"the name of the company is Tesla,whose owner is elon musk and he
is the world's richest man'''

company=input("enter the company name")
name=input("enter the name")
rank=input("enter his rank in world'richest man")


templates="The name of the company is{},whose owner is{} and rank as {} in world richest man chart".format(company,name,rank)
print(templates)