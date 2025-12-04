#python function to convert inches to cms
#cm=inc*2.54
def inc_to_cm(inc):
    return inc*2.54
inc=6
cm=inc_to_cm(inc)
print("conversion of inches to cm is " + str(cm))