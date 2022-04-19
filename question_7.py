# coding: utf-8


# どちらのメソッドでも大丈夫です
# Either method is fine

def bmi(height, weight):
  return weight / (height / 100) ** 2 


def bmi_2(height, weight):
  return 10_000 * weight / height ** 2


print(bmi(187, 62))
print(bmi_2(187, 62))
