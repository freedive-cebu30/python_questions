# coding: utf-8


dict_1 = { 'name': 'Taro', 'age': 20, 'height': 180, 'weight': 60 }
dict_2 = { 'name_2': 'Jiro', 'age_2': 30, 'height_2': 170, 'weight_2': 50 }

dict_3 = {**dict_1, **dict_2}
print(dict_3)

dict_1.update(dict_2)
print(dict_1)
