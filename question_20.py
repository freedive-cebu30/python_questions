# coding: utf-8

# リスト内包表記
# list Inclusive
arr = [1, 2, 3, 4, 5]
double_arr = [value * 2 for value in arr]
print(double_arr)


# mapとlambda式
# map and lambda
double_arr_2 = list(map(lambda x: x * 2, arr))
print(double_arr_2)


# mapとユーザー定義関数
# map and function
def double(n):
  return n * 2

double_arr_3 = list(map(double, arr))
print(double_arr_3)


# forループ
# for loop
double_arr_4 = []
for value in arr:
    double_arr_4.append(value * 2)

print(double_arr_4)
