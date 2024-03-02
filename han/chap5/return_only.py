def return_test():
    print("A")
    return
    print("B")
    
return_test()

def return_test() -> str:
    return "A"

print(return_test())

def return_test() -> None:
    return

print(return_test())

    