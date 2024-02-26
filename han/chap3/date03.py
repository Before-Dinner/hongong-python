import datetime

now = datetime.datetime.now()

if 3 <= now.month <= 5:
  print("봄 {}".format(now.month))
if 6 <= now.month <= 8:
  print("여름 {}".format(now.month))
if 9 <= now.month <= 11:
  print("가을 {}".format(now.month))
if now.month == 12 or now.month <= 2:
  print("겨울 {}".format(now.month))