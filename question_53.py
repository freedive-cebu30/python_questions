# coding: utf-8


import random, string

def random_small_letters(n):
   randlst = [random.choice(string.ascii_letters[0:26]) for i in range(n)]
   return ''.join(randlst)
   

def random_big_letters(n):
   randlst = [random.choice(string.ascii_letters[26:52]) for i in range(n)]
   return ''.join(randlst)

print(random_small_letters(10))
print(random_big_letters(10))
