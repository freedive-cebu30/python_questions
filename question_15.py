# coding: utf-8

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_v = max(num)
print(max_v)


max_v = 0
for v in num:
  if max_v < v:
    max_v = v
  
print(max_v)
