# coding: utf-8


arr = [1, "a", 2, "b", "c", 3]

# forループ
# for loop
res = []
for v in arr:
  if type(v) is int:
    res.append(v)

print(res)


# filterとlambda式
# filter and lambda
answer1 = list(filter(lambda v: type(v) is int, arr))
print(answer1)


# リスト内包表記
# list Inclusive
answer2 = [type(v) is int for value in arr]
print(answer1)
