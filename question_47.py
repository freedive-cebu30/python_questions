# coding: utf-8


def test(*val):
  print(val)
  print(type(val))
  
  
def test2(**val):
  print(val)
  print(type(val))


test(1)
test(1, 2, 3)
test(1, 2, 3, 4)


test2(key1=1)
test2(key1=1, key2=2)
test2(key1=1, key2=2, key3=3)
