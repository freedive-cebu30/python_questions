# coding: utf-8

# どちらのメソッドでも大丈夫ですが、条件分岐が単純な場合は1行が好まれる傾向にあります。
# Either way is fine. However, if condition is simple, we prefer "one line".

def check_alcohol(age):
  message =  'OK' if age > 19 else 'NG'
  
  return message

def check_alcohol_if(age):
  if age > 19:
    return 'OK'
  else:
    return 'NG'


message = check_alcohol(19)
print(f'あなたの場合は、お酒は{message}です')
message = check_alcohol_if(20)
print(f'あなたの場合は、お酒は{message}です')
