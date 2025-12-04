#program to convert celsius to fahrenheit
# F = (°C × 9/5) + 32
def conv_cel_to_fah(c):
  F= (c * 9/5) + 32
  return F

fah=conv_cel_to_fah(47)
print("celsius to fahrenheit is: " + str(fah))
