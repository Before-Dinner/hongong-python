list_a = [0, 1, 2, 3, 4, 5]

del list_a[1:2]
print("del list_a[1]:", list_a)

list_a.pop(2)
print("pop(2):", list_a)

list_a.remove(5)
print("remove(5):", list_a)

print(list_a[-1])
print(list_a[::-1])