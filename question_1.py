# coding: utf-8

number1 = 2
number2 = 3
number3 = 10
number4 = 10_000

# f-string
print(f'{number3} + {number2} = {number3 + number2}')
print(f'{number3} - {number2} = {number3 - number2}')
print(f'{number3} × {number2} = {number3 * number2}')
print(f'{number4} ÷ {number3} = {number4 / number3}')
print(f'{number3} ÷ {number2} = {number3 / number2} 余り {number3 % number2}')
print(f'{number3} ÷ {number2} = {number3 // number2} 余り {number3 % number2}')
print(f'{number1}の2乗 = {number1 ** 2}')
print(f'{number1}の3乗 = {number1 ** 3}')


# Templateを使って、書くこともできます
# You can write a code by Template
from string import Template
t = Template('${first} + ${second} = ${third}')
print(t.substitute(first=number3, second=number2, third = number3 + number2))


# formatを使って、書くこともできます
# You can write a code by format
print('{} - {} = {}'.format(number3, number2, number3 - number2))


# %を使って、書くこともできます
# You can write a code by %
print('%s * %s = %s' % (number3, number2, number3 * number2))
