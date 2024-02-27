score = float(input("학점> "))

if score == 4.5:
  print(1)
elif 4.2 <= score < 4.5:
  print(2)
elif 3.5 <= score < 4.2:
  print(3)
elif 2.8 <= score < 3.5:
  print(4)
elif 2.3 <= score < 2.8:
  print(5)
elif 1.75 <= score < 2.3:
  print(6)
elif 1.0 <= score < 1.75:
  print(7)
elif 0.5 <= score < 1.0:
  print(8)
elif 0 <= score < 0.5:
  print(9)
elif score == 0:
  print(10)