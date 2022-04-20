# coding: utf-8


fruits = ['apple', 'apple', 'orange', 'mango', 'mango', 'mango', 'mango']

res = {}
for fruit in fruits:
  if fruit in res:
    res[fruit] += 1
  else:
    res[fruit] = 1
    
print(res)

res = {} 
for fruit in fruits:
  if fruit in res:
    res[fruit] += 1
  else:
    res.setdefault(fruit, 1)
