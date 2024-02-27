dictionary = {
    "name": "han",
    "age": 28
}

key = input("key> ")
value = dictionary.get(key)
print(value)

if value == None:
    print("key is none")
