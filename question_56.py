# coding: utf-8


people = [{ 'name': 'Taro_1', 'age': 20, 'height': 180, 'weight': 60 },
          { 'name': 'Taro_2', 'age': 40, 'height': 160, 'weight': 70 },
          { 'name': 'Taro_3', 'age': 50, 'height': 150, 'weight': 75 }
         ]
         

class Person():
  def __init__(self, name, age, height, weight):
    self.name = name
    self.age = age
    self.height = height
    self.weight = weight

  def bmi(self):
    print(self.weight / (self.height / 100) ** 2)
    
  def show_status(self):
    print(f'name {self.name}, age: {self.age}')


for person in people:
  person = Person(person["name"], person["age"], person["height"], person["weight"])
  person.bmi()
  person.show_status()
