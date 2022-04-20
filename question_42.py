# coding: utf-8


fruits = [ {'apple': 100, 'orange': 50, 'mango': 30},
           {'apple': 200, 'orange': 250, 'mango': 230},
           {'apple': 300, 'orange': 350, 'mango': 330},
         ]

total = 0
for fruit in fruits:
  total += fruit['apple']

print(total)


# reduceを使って書くこともできます
# You can write a code by reduce
from functools import reduce
total2 = reduce(lambda total, fruit: total + fruit['apple'], fruits, 0)
print(total2)
