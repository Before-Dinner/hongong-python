def print_n_times_parmas(num: int, *params: str) -> None:
    for i in range(num):
        print(*params) # flat 하게 사용
    
print_n_times_parmas(5, "wow", "good")

def print_n_times_parmas(num: int, *params: str) -> None:
    for i in range(num):
        for value in params:
            print(value, end = " ") 
        print()

print_n_times_parmas(5, "yo", "hmm")

def print_n_times_parmas(*params: str, num=2) -> None:
    for i in range(num):
        print(*params) # flat 하게 사용
        
print_n_times_parmas("come", "on")