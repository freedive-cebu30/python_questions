# coding: utf-8


people = [{ 'name': 'Taro_1', 'age': 20, 'height': 180, 'weight': 60 },
          { 'name': 'Taro_2', 'age': 40, 'height': 160, 'weight': 70 },
          { 'name': 'Taro_3', 'age': 50, 'height': 150, 'weight': 75 }
         ]
         
def bmi(height, weight):
  return weight / (height / 100) ** 2 

for person in people:
  print(f'name {person["name"]}, age: {person["age"]}')
  print(f'BMI {bmi(person["height"], person["weight"])}')
