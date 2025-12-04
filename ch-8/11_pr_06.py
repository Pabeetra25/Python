''' python function to remove a given word from thw string
 and strip it at the same time'''
# country="       Nepal is a land-locked    "
# print(country)
# print(country.strip())
def remove_and_split(string,word):
  newstr=string.replace(word,"")
  return newstr.strip()

country="       Nepal is a land-locked    "
m=remove_and_split(country,"Nepal")
print(m)