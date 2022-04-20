# coding: utf-8


import random


# Setという概念を使えば、重複しない集合を作ることができます
# We can create a set without repetition if we use "Set"
res = set()
for x in range(1, 21):
  res.add(random.randint(1, 10))
  

list_res = list(res)
list_res.sort()
print(list_res)



# 配列に入れる前に、既に値が入っているか確認しています
# We check the value in Array before adding the value
res2 = []
for x in range(1, 21):
  val = random.randint(1, 10)
  if (val not in res2):
    res2.append(val)

res2.sort()
print(res2)
