dictionary = {
    "name": "한성덕",
    "age": 28,
    "info": ["한성덕", 28],
    2: 32
}

print("{} + {}".format(dictionary["info"][0], dictionary["info"][1]))
dictionary["info"].append("ansan")
dictionary["info"].append([2,3])
print(dictionary)
dictionary["info"][-1] = '010-2587-8195'
print(dictionary)