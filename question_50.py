# coding: utf-8


from datetime import datetime, date, timedelta

today = datetime.today()
yesterday = today - timedelta(days = 1)
tomorrow = today + timedelta(days = 1)


print(datetime.strftime(yesterday, '%Y-%m-%d'))
print(datetime.strftime(today, '%Y-%m-%d'))
print(datetime.strftime(tomorrow, '%Y-%m-%d'))
