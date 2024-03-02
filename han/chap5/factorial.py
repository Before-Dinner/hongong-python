def factorial(n:int) -> int:
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorial(5))

def factorial_2(n:int) -> int:
    return 1\
        if n == 1\
        else n * factorial_2(n-1)
    
    if n == 1:
        return 1
    else:
        return n * factorial_2(n-1) 
    
print(factorial_2(5))