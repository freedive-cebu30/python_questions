# coding: utf-8


dict_people = [{ 'name': 'Taro_1', 'age': 20, 'height': 180, 'weight': 60, 'country': 'Japan' },
               { 'name': 'Taro_2', 'age': 30, 'height': 170, 'weight': 65 },
               { 'name': 'Taro_3', 'age': 40, 'height': 160, 'weight': 70, 'country': 'Taiwan'},
               { 'name': 'Taro_4', 'age': 50, 'height': 150, 'weight': 75, 'country': 'Japan' }]

res = []
for person in dict_people:
  if 'country' in person:
    res.append(person)

print(res)

# リスト内包表記
# list Inclusive
res2 = [person for person in dict_people if 'country' in person]
print(res2)


# filter
# filter and lambda
res3 = list(filter(lambda person: 'country' in person, dict_people))
print(res3)
