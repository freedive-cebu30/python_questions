# coding: utf-8


def fizz_buzz(n):
  if n % 15 == 0:
    return 'FizzBuzz'
  elif n % 5 == 0:
    return  'Buzz'
  elif n % 3 == 0:
    return 'Fizz'
  else:
    return n

print(fizz_buzz(2))
print(fizz_buzz(3))
print(fizz_buzz(5))
print(fizz_buzz(15))

# 2
# Fizz
# Buzz
# FizzBuzz
