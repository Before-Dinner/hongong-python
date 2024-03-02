def sum_all(a: int, b: int ,c: int) -> int:
    sum = 0
    for i in range(a, b + 1, c):
        sum += i
    return sum

print(sum_all(0, 100, 1))
print(sum_all(0, 1000, 1))
print(sum_all(50, 100, 1))
print(sum_all(500, 1000, 1))

def sum_all(a: int, b=100 ,c=1) -> int:
    sum = 0
    for i in range(a, b + 1, c):
        sum += i
    return sum

print(sum_all(0, 100, 2))