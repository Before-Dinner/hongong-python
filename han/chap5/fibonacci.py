def fibonacci(n: int) -> int:
    global count
    count += 1
    return 1\
        if n == 1 or n == 2\
        else fibonacci(n-1) + fibonacci(n-2) 
    
# print(fibonacci(5))
count = 0

def fibonacci2(n: int) -> int:
    return fibonacci(n)
    
print(fibonacci2(10), "{}".format(count))

dictionary = {
    1: 1,
    2: 2
}

def fibonacci3(n: int) -> int:
    if n in dictionary:
        return dictionary[n]
    
    else:
        dictionary[n] = fibonacci(n)
        return dictionary[n]
    