# coding: utf-8


import unittest

unit = unittest.TestCase()


def fizz_buzz(n):
  try:
    if n < 1:
      raise Exception("Don't enter this value. minimum 0")
    if n % 15 == 0:
      return 'FizzBuzz'
    elif n % 5 == 0:
      return  'Buzz'
    elif n % 3 == 0:
      return 'Fizz'
    else:
      return n
  except Exception as e:
    print(e)
    return n

unit.assertEqual(fizz_buzz(-1), -1)
unit.assertEqual(fizz_buzz(2), 2)
unit.assertEqual(fizz_buzz(3), 'Fizz')
unit.assertEqual(fizz_buzz(5), 'Buzz')
unit.assertEqual(fizz_buzz(15), 'FizzBuzz')

unittest.main()
