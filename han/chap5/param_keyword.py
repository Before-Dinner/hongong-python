import math
def print_n_times_parmas(*params: str, num=2) -> None:
    for i in range(num):
        print(*params) # flat 하게 사용
        
print_n_times_parmas("come", "on", 4, num=2)


def test(a: int, b=2, c=100) -> int:
    return a + b + c

print(test(1, 2, 3))
print(test(1, b=3, c=200))
print(test(b=3, c=200, a=1))