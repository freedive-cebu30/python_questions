# coding: utf-8


def cal(number):
  s_number = str(number)
  three_times_number = s_number * 3
  i_number = int(three_times_number)

  return number + i_number

print(cal(3))
print(cal(4))
print(cal(10))
