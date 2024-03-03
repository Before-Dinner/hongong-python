import random

file = open("basic.txt", "w")
file.write("hello")
file.close()

with open("basic.txt", "r") as file:
  contents = file.read()

print(contents)

hanguls = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

with open("info.txt", "w") as file:
  for i in range(5):
    name = random.choice(hanguls) + random.choice(hanguls)
    weight = random.randrange(40, 100)
    height = random.randrange(140, 200)
    file.write("{}, {}, {}\n".format(name, weight, height))
    
with open("info.txt", "r") as file:
  contents = file.read()

print(contents)