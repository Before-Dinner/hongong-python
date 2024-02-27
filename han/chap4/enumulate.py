example_list = ["A", "B", "C"]

enum = enumerate(example_list)
print(enum)

enum = list(enum)
print(enum)

for i, v in enumerate(example_list):
    print(i, end=" ")
    print(v)