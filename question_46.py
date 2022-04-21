# coding: utf-8


def check_3_5_multiple_1(number):
  if number % 3 == 0 or number % 5 == 0:
    return True
  else:
    return False

def check_3_5_multiple_2(number):
  if number % 3 != 0 and number % 5 != 0:
    return False
  else:
    return True

print(check_3_5_multiple_1(9))
print(check_3_5_multiple_1(10))
print(check_3_5_multiple_1(14))
print(check_3_5_multiple_1(15))
print(check_3_5_multiple_1(30))

print(check_3_5_multiple_2(9))
print(check_3_5_multiple_2(10))
print(check_3_5_multiple_2(14))
print(check_3_5_multiple_2(15))
print(check_3_5_multiple_2(30))
