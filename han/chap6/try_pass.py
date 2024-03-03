list_input_a = ["52", "273", "32", "스파이", "103"]

list_number = []
for item in list_input_a:
  try:
    int(item)
    list_number.append(item)
  except:
    pass

print("{}".format(list_input_a))
print("{} number".format(list_number))