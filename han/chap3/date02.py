import datetime

now = datetime.datetime.now()

if now.hour < 12:
  print("오전 {}".format(now.hour))

if now.hour >= 12:
  print("오후 {}".format(now.hour))
