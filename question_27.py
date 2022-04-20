# coding: utf-8


arr = ["090-1111-22223", "090-1111-22224", "090-1111-22225"]


# filterとlambda式
# filter and lambda
answer1 = list(map(lambda v: v.replace('-', ''), arr))
print(answer1)


# リスト内包表記
# list Inclusive
answer2 = [v.replace('-', '') for v in arr]
print(answer2)


# forループ
# for loop
res = []
for v in arr:
  val = v.replace('-', '')
  res.append(val)

print(res)
