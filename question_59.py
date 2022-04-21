# coding: utf-8


import unittest
unit = unittest.TestCase()


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


unit.assertEqual(check_3_5_multiple_1(9), True)
unit.assertEqual(check_3_5_multiple_1(10), True)
unit.assertEqual(check_3_5_multiple_1(14), False)
unit.assertEqual(check_3_5_multiple_1(15), True)
unit.assertEqual(check_3_5_multiple_1(30), True)
unit.assertEqual(check_3_5_multiple_1(31), False)

unit.assertEqual(check_3_5_multiple_2(9), True)
unit.assertEqual(check_3_5_multiple_2(10), True)
unit.assertEqual(check_3_5_multiple_2(14), False)
unit.assertEqual(check_3_5_multiple_2(15), True)
unit.assertEqual(check_3_5_multiple_2(30), True)
unit.assertEqual(check_3_5_multiple_2(31), False)

unittest.main()
