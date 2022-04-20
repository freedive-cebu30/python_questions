# coding: utf-8


fruits = {"apple": 100, "mango": 200, "banana": 400, "orange": 300}
max_kv = max(fruits.items(), key=lambda v: v[1])
dct = dict([max_kv])

print(dct)
