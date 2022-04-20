# coding: utf-8

list_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

n = 4
res = [tuple(list_num[i: i+n]) for i in range(0, len(list_num), n)]
print(res)


res2 = []
for i in range(0, len(list_num), 4):
  res2.append(tuple(list_num[i: i+n]))

print(res2)
