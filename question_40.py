# coding: utf-8


fruits = {"apple": 100, "mango": 200, "banana": 400, "orange": 300}
min_kv = min(fruits.items(), key=lambda v: v[1])
dct = dict([min_kv])

print(dct)
