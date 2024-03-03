try:
  number_input_a = int(input("> "))
except:
  print("X")
else:
  print("r:", number_input_a)
  print("l:", 2 * 3.14 * number_input_a)
  print("w:", 3.14 * number_input_a * number_input_a)
  
try:
  number_input_a = int(input("> "))
except:
  print("X")
else:
  print("r:", number_input_a)
  print("l:", 2 * 3.14 * number_input_a)
  print("w:", 3.14 * number_input_a * number_input_a)
finally:
  print("done")