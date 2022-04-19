# coding: utf-8


def cal_abs(number_1, number_2):
  answer = number_1 - number_2
  return abs(answer) if (answer < 0) else answer


print(cal_abs(10, 5))
print(cal_abs(10, 13))
