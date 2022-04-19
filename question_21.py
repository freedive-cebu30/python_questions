# coding: utf-8

arr1 = [1, 2, 3, 4, 5, 8, 9, 10, 18, 20]
arr2 = [1, 2, 3, 4, 5, 8, 10, 20]

# filterとlambda式
# filter and lambda
answer1 = next(filter(lambda v: v % 9 == 0, arr1), None)
print(answer1)

answer2 = next(filter(lambda v: v % 9 == 0, arr2), None)
print(answer2)

# ジェネレーター
# generators
answer3 = next((v for v in arr1 if v % 9 == 0), None)
print(answer3)

answer4 = next((v for v in arr2 if v % 9 == 0), None)
print(answer4)


# forループ
# for loop
def detect(arr):
  for v in arr:
    if v % 9 == 0:
      return v
  
  return None

answer5 = detect(arr1)
print(answer5)

answer6 = detect(arr2)
print(answer6)    
