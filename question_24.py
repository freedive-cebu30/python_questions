# coding: utf-8


arr = [1, "a", 2, "b", "c", 3, "4", "5", "6"]

def is_int(v):
  if type(v) is int:
    return v
  elif type(v) is str and v.isdigit():
    return v


# forループ
# for loop
string_list = []
for v in arr:
  if is_int(v):
    string_list.append(v)

cast_list = list(map(int, string_list))
cast_list.sort(reverse=True)
print(cast_list)


# filterと関数
# filter and function
string_list = list(filter(is_int, arr))
print(string_list)


# # リスト内包表記
# # list Inclusive
string_list = [v for v in arr if is_int(v)]
print(string_list)
