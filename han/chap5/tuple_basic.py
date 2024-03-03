[a, b] = [1, 2]
c = (3, 5)
d = (3, )

print(type(c))
print(c)

i, k = 1, 2

print(type(i), type(k))
print(i, k)

i, k = k, i

print(type(i), type(k))
print(i, k)

def test() -> tuple:
    return 1, "str"

print(type(test()))
a, b = test()
print(type(a), type(b))
print(a, b)