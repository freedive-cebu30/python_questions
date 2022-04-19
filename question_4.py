# coding: utf-8

def modulus(mod):
  if mod > 25:
    return False
  
  for number in range(1, 26):
    if number % mod == 0:
      print(number) 

modulus(5)
modulus(7)
modulus(26)
