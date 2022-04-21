# coding: utf-8


def get_generator():
  for v in range(1, 6):
    yield v


def display_number():
  gen = get_generator()
  for v in gen:
    print(v)

def sum_number():
  val = 0
  gen = get_generator()
  for v in gen:
    val += v
  
  return val

def multiply_number():
  val = 1
  gen = get_generator()
  for v in gen:
    val *= v

  return val


display_number()
print(sum_number())
print(multiply_number())
