import datetime
start_time = datetime.datetime(2020, 3, 1)
how_long = start_time - datetime.datetime.now()

print(type(how_long))
print(how_long.days)
print(how_long.seconds)
print("3월 1일까지는 {}일 {}시간 남았습니다.".format(how_long.days, how_long.seconds//3600))

hundred = datetime.timedelta(days=100)
print(datetime.datetime.now()+hundred)
print(datetime.datetime.now()-hundred)

tomorrow = datetime.datetime.now().replace(hour=9, minute=0, second=0) + datetime.timedelta(days=1)
print(tomorrow)