# coding: utf-8


lang = ["ruby", "php", "python", "java", "javascript"]
print(list(map(str.capitalize, lang)))

res = []

for v in lang:
  res.append(v.capitalize())

print(res)
