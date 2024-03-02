import math
dictionary = {
    "name": "han",
    "age": 28
}

key = input("key> ")

if key in dictionary: print(True)
else: print(False)

arr = [1,2,3,4]

temp = []
for a in arr:
    if a != 4:
        temp.append(a)
        
temp = [a for a in arr if a != 4]
print(temp)

result = True \
        if 2 == math.sqrt(4) \
        else False

print(result)