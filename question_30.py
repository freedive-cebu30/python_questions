# coding: utf-8

v_1 = [1, 2, 3, 4, 5, 8, 9]
v_2 = [9, 7, 6, 5, 4]

set_1 = set(v_1)
set_2 = set(v_2)

answer = set_1 ^ set_2
print(answer)
print(list(answer))


answer2 = set_1.symmetric_difference(set_2)
print(answer2)
print(list(answer2))
