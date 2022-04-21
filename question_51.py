# coding: utf-8


def display_number():
  for v in range(1, 6):
    print(v)

def sum_number():
  val = 0
  for v in range(1, 6):
    val += v
  
  return val

def multiply_number():
  val = 1
  for v in range(1, 6):
    val *= v

  return val

display_number()
print(sum_number())
print(multiply_number())
