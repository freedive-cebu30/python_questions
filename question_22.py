# coding: utf-8

import random

sample_arr = []
while True:
  for x in range(10):
    sample_arr.append(random.randint(1, 30))

  if next(filter(lambda v: v % 11 == 0, sample_arr), None):
    break
  
  sample_arr = []

print(sample_arr)
