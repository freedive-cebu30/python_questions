# coding: utf-8

lang = ['Ruby', 'Php', 'Python', 'Java', 'Javascript']
ascending_order_value = sorted(lang, key=len)
print(ascending_order_value)

descending_order_value = sorted(lang, key=len, reverse=True)
print(descending_order_value)
