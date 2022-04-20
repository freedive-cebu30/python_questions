# coding: utf-8


arr = ["Ms. Tanaka", "Mr. Suzuki", "Ms. Akagi", "Mrs. Yoko"]


# filterとlambda式
# filter and lambda
answer1 = list(filter(lambda v: v.startswith('Ms.'), arr))
print(answer1)

answer2 = list(filter(lambda v: v.endswith('i'), arr))
print(answer2)


# リスト内包表記
# list Inclusive
answer3 = [v for v in arr if v.startswith('Ms.')]
print(answer3)

answer4 = [v for v in arr if v.endswith('i')]
print(answer4)


# forループ
# for loop
res = []
for v in arr:
  if v.startswith('Ms.'):
    res.append(v)

print(res)

res2 = []
for v in arr:
  if v.endswith('i'):
    res2.append(v)

print(res2)
