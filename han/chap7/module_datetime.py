import datetime

now = datetime.datetime.now()
print(now.year)
print(now.hour)
print(now.day)
print(now.month)
print(now.minute)
print(now.second)

#1
print(now.strftime("%Y.%m.%d %H:%M:%S"))
#2
print(now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format("year", "month", "day", "hour", "minute", "second"))

after = now + datetime.timedelta(weeks=1,
                                 days=1,
                                 hours=1,
                                 minutes=1,
                                 seconds=1)

print(after.strftime("%Y.%m.%d %H:%M:%S")) 
print(now.replace(now.year + 1))

