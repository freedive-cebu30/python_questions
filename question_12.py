# coding: utf-8

# どちらの方法でも大丈夫です
# either way is fine
def compare_string(string_1, string_2):
  list_1 = list(string_1)
  list_2 = list(string_2)
    
  res = []
  for v1 in list_1:
    for v2 in list_2:
      if v1 == v2:
        res.append(v1)
  
  return res
  
# Setという概念を使って共通部分を取得しています
# We get common part by using Set
def compare_string_by_set(string_1, string_2):
  list_1 = list(string_1)
  list_2 = list(string_2)
    
  return list(set(list_1) & set(list_2))
        
  
print(compare_string("rubys", "rails"))
print(compare_string_by_set("rubys", "rails"))
