dictionary = {
    "A": "a",
    "B": "b",
    "C": "c"
}

values = dictionary.items()
print(values)

for i,v in values:
    print("key :{} value :{}".format(i, v))
