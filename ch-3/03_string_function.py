from itertools import count
from time import process_time_ns


poem='''muna madan is the very beautiful and the emotional poem written
mahakabi'''
#string function
print(len(poem))
print(poem.endswith('mahakabi'))
print(poem.capitalize())
print(poem.count('the'))
print(poem.count('a'))
print(poem.find('madan'))#(if not find return -1 as output)
print(poem.replace('mahakabi','greatkabi'))