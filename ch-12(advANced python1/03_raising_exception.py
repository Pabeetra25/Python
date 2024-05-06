def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Exception occured:")

a=increment('asd45')
print(a)        