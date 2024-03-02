def print_3_times():
    print("hi")
    print("hi")
    print("hi")
    
print_3_times()

def print_n_times(str: str, n: int) -> None:
    for i in range(n+1):
        print(str, end = " ")
        
print_n_times("Hi", 5)

