# coding: utf-8


arr = ["Taiwan-tokyo", "Taiwan-osaka", "Taiwan-kyoto"]


# mapとlambda式
# map and lambda
answer1 = list(map(lambda v: v.replace('Taiwan', 'Japan'), arr))
print(answer1)


# リスト内包表記
# list Inclusive
answer2 = [v.replace('Taiwan', 'Japan') for v in arr]
print(answer2)


# forループ
# for loop
res = []
for v in arr:
  val = v.replace('Taiwan', 'Japan')
  res.append(val)

print(res)
