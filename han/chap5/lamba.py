from typing import Callable
import math

def test() -> None:
    print("TEST")
    
def ten_print_test(func: Callable[[], None]) -> None:
    n = 0
    while n < 10:
        func()
        n+=1
    
ten_print_test(test)

def power(item: int) -> int:
    return pow(item, 2)

def under_3(item: int) -> bool:
    return item < 3

list_a = [1, 2, 3, 4, 5, 6]

print(list(map(power, list_a)))
print(list(filter(under_3, list_a))) 

print(list(map(
    lambda x: pow(x, 2), 
    list_a)))

print(list(filter(
    lambda x: x < 3, 
    list_a)))

print(list(map(
    lambda x: pow(x, 2), 
    list(filter(
        lambda x: x < 5, 
        list_a)))))
